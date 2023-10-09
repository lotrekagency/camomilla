from collections import defaultdict
from inspect import isclass
from typing import Any, Dict, Sequence
from typing_extensions import get_args, get_origin
from camomilla.settings import STRUCTURED_FIELD_CACHE_ENABLED
from camomilla.structured.fields import ForeignKey, QuerySet
from camomilla.structured.models import BaseModel
from camomilla.structured.utils import _LazyType, get_type, pointed_setter
from django.db.models import Model as DjangoModel
from camomilla.utils.getters import pointed_getter
from typing import Iterable, Union


# TODO:
# ::: Actually this is a first draft.
# The system should be more type safe.
# It should handle initialization made with model instance not only dicts
# Neet to check if there are problems with different formats for pks (model instaces or string or dicts)


class Cache(dict):
    pass


class ValueWithCache:
    def __init__(self, cache, model, value) -> None:
        self.cache: Cache = cache
        self.value: Union[Iterable[Union[str, int]], str, int] = value
        self.model: type[DjangoModel] = model

    def retrieve(self):
        cache = self.cache.get(self.model)
        if hasattr(self.value, '__iter__'):
            qs = self.model.objects.filter(pk__in=self.value)
            setattr(
                qs,
                "_result_cache",
                [cache[i] for i in self.value if i in cache] if cache else [],
            )
            return qs
        else:
            val = cache.get(self.value, None)
            if val is None:
                return self.model._default_manager.get(pk=self.value)
            else:
                return val


class RelInfo:
    FKField: str = "fk"
    QSField: str = "qs"
    RIField: str = "rel"
    RLField: str = "rel_l"

    def __init__(self, model, type, field) -> None:
        self.model = model
        self.type = type
        self.field = field


class CacheBuilder:
    def __init__(self, related_fields: Dict[str, RelInfo]) -> None:
        self.__related_fields__ = related_fields

    @classmethod
    def from_model(cls, model: BaseModel) -> "CacheBuilder":
        return cls(related_fields=cls.inspect_related_fields(model))

    @classmethod
    def inspect_related_fields(cls, model: type[BaseModel]) -> Dict[str, RelInfo]:
        related = {}
        for field_name, field in model.model_fields.items():
            annotation = field.annotation
            origin = get_origin(annotation)
            args = get_args(annotation)

            if isclass(origin) and issubclass(origin, ForeignKey):
                related[field_name] = RelInfo(
                    get_type(annotation), RelInfo.FKField, field
                )
            elif isclass(origin) and issubclass(origin, QuerySet):
                related[field_name] = RelInfo(
                    get_type(annotation), RelInfo.QSField, field
                )

            elif isclass(origin) and issubclass(origin, Sequence):
                lazy_types = [
                    _LazyType(arg).evaluate(model)
                    for arg in args
                    if isinstance(arg, str)
                ]
                subclass = next(
                    (
                        c
                        for c in list(args) + lazy_types
                        if isclass(c) and issubclass(c, BaseModel)
                    ),
                    None,
                )
                if isclass(subclass) and issubclass(subclass, BaseModel):
                    related[field_name] = RelInfo(subclass, RelInfo.RLField, field)

            elif isclass(annotation) and issubclass(annotation, BaseModel):
                related[field_name] = RelInfo(annotation, RelInfo.RIField, field)
        return related

    def get_all_fk_data(self, data):
        if isinstance(data, Sequence):
            fk_data = defaultdict(list)
            for index in range(len(data)):
                child_fk_data = self.get_all_fk_data(data[index])
                for model, touples in child_fk_data.items():
                    fk_data[model] += [(f"{index}.{t[0]}", t[1]) for t in touples]
            return fk_data
        return self.get_fk_data(data)

    def get_fk_data(self, data):
        fk_data = defaultdict(list)
        if not data:
            return fk_data
        for field_name, info in self.__related_fields__.items():
            if info.type == RelInfo.FKField:
                value = pointed_getter(data, field_name, None)
                if value:
                    if isinstance(
                        value, ValueWithCache
                    ):  # needed to break recursive cache builds
                        fk_data = {}
                        break
                    fk_data[info.model].append(
                        (
                            field_name,
                            pointed_getter(value, info.model._meta.pk.attname, value),
                        )
                    )
            elif info.type == RelInfo.QSField:
                value = pointed_getter(data, field_name, [])
                if isinstance(value, list):
                    if any(
                        True for v in value if isinstance(v, ValueWithCache)
                    ):  # needed to break recursive cache builds
                        fk_data = {}
                        break
                    fk_data[info.model].append(
                        (
                            field_name,
                            [
                                pointed_getter(i, info.model._meta.pk.attname, i)
                                for i in value
                                if i
                            ],
                        )
                    )

            elif info.type == RelInfo.RLField:
                values = pointed_getter(data, field_name, [])
                if isinstance(values, list):
                    for index in range(len(values)):
                        for model, touples in (
                            self.from_model(info.model)
                            .get_all_fk_data(values[index])
                            .items()
                        ):
                            fk_data[model] += [
                                (f"{field_name}.{index}.{t[0]}", t[1]) for t in touples
                            ]
            elif info.type == RelInfo.RIField:
                value = pointed_getter(data, field_name, None)
                child_fk_data = self.from_model(info.model).get_all_fk_data(value)
                for model, touples in child_fk_data.items():
                    fk_data[model] += [(f"{field_name}.{t[0]}", t[1]) for t in touples]
        return fk_data

    def inject_cache(self, data: Any) -> Any:
        if not STRUCTURED_FIELD_CACHE_ENABLED:
            return data
        fk_data = self.get_all_fk_data(data)
        plainset = defaultdict(set)
        for model, touples in fk_data.items():
            for t in touples:
                if isinstance(t[1], Sequence):
                    plainset[model].update(t[1])
                else:
                    plainset[model].add(t[1])
        cache = Cache()
        for model, values in plainset.items():
            models = []
            pks = []
            for value in values:
                if isinstance(value, model):
                    models.append(value)
                else:
                    pks.append(value)
            models_pks = [m.pk for m in models]
            pks = [pk for pk in pks if pk not in models_pks]
            if len(pks):
                models += list(model.objects.filter(pk__in=pks))
            cache[model] = {obj.pk: obj for obj in models}

        for model, touples in fk_data.items():
            for t in touples:
                pointed_setter(data, t[0], ValueWithCache(cache, model, t[1]))
        return data
