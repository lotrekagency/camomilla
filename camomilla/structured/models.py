from collections import defaultdict
from jsonmodels.models import Base
from jsonmodels.fields import _LazyType
from jsonmodels.validators import ValidationError
from camomilla.structured.fields import (
    ForeignKey,
    ForeignKeyList,
    EmbeddedField,
    ListField,
)
from camomilla.utils.getters import pointed_getter

__all__ = ["Model"]


class _Cache:
    instance = None
    parent = None
    prefetched_data = {}

    def __init__(self, instance):
        self.instance = instance
        self.prefetched_data = {}

    @property
    def is_root(self):
        return self.parent == None

    @property
    def root_node(self):
        root = self.instance
        while root._cache.parent is not None:
            root = root._cache.parent
        return root

    def get_prefetched_data(self):
        if self.is_root:
            return self.prefetched_data
        return self.root_node.get_prefetched_data()


class Model(Base):
    def __init__(self, **kwargs):
        self._cache = _Cache(self)
        for _, field in self.iterate_over_fields():
            field.bind(self)
        super(Model, self).__init__(**kwargs)

    def populate(self, **kwargs):
        relations = self.prepopulate(**kwargs)
        self.prefetch_related(kwargs)
        super(Model, self).populate(**relations)

    def prepopulate(self, **kwargs):
        relations = {}
        for _, struct_name, field in self.iterate_with_name():
            if struct_name in kwargs and isinstance(
                field, (ForeignKey, ForeignKeyList, EmbeddedField, ListField)
            ):
                relations[struct_name] = kwargs.pop(struct_name)
        super(Model, self).populate(**kwargs)
        return relations

    def bind(self, parent):
        self._cache.parent = parent

    @classmethod
    def to_db_transform(cls, data):
        return data

    @classmethod
    def from_db_transform(cls, data):
        return data

    @classmethod
    def get_all_relateds(cls, struct):
        relateds = defaultdict(set)
        for _, struct_name, field in cls.iterate_with_name():
            if isinstance(field, ForeignKey):
                value = struct.get(struct_name, None)
                model = getattr(field, "model", None)
                if value:
                    relateds[model].add(value)
            elif isinstance(field, ForeignKeyList):
                value = pointed_getter(struct, struct_name, [])
                if isinstance(value, list):
                    model = getattr(field, "inner_model", None)
                    relateds[model].update([i for i in value if i])
            elif isinstance(field, ListField):
                values = pointed_getter(struct, struct_name, [])
                if isinstance(values, list):
                    for val in values:
                        if isinstance(val, Model):
                            main_type = val.__class__
                            val = val.to_struct()
                        else:
                            main_type = field._get_main_type()
                            if isinstance(main_type, _LazyType):
                                main_type = main_type.evaluate(cls)
                        if issubclass(main_type, Model):
                            for model, pks in main_type.get_all_relateds(val).items():
                                relateds[model].update(pks)
            elif isinstance(field, EmbeddedField):
                value = struct.get(struct_name, None)
                if isinstance(value, Model):
                    value = value.to_struct()
                if not isinstance(value, dict):
                    continue
                child_relateds = field._get_embed_type().get_all_relateds(value)
                for model, pks in child_relateds.items():
                    relateds[model].update(pks)
        return relateds

    def prefetch_related(self, struct):
        if struct.keys() and self._cache.is_root:
            relateds = self.get_all_relateds(struct)
            for model, pks in relateds.items():
                self._cache.prefetched_data[model] = (
                    {obj.pk: obj for obj in build_model_cache(model, pks)}
                    if len(pks) > 0
                    else {}
                )

    def get_prefetched_data(self):
        return self._cache.get_prefetched_data()


def build_model_cache(model, values):
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
    return models
