from inspect import isclass
from typing import Any, Dict, Tuple, get_origin

import pydantic._internal._model_construction
from django.db.models import Model as DjangoModel
from pydantic import BaseModel as PyDBaseModel
from pydantic import Field, model_validator
from typing_extensions import Annotated

from .fields import ForeignKey, QuerySet
from .utils import get_type, map_method_aliases


class BaseModelMeta(pydantic._internal._model_construction.ModelMetaclass):
    def __new__(
        mcs, name: str, bases: Tuple[type], namespaces: Dict[str, Any], **kwargs
    ):
        annotations: dict = namespaces.get("__annotations__", {})
        for base in bases:
            for base_ in base.__mro__:
                if base_ is PyDBaseModel:
                    break
                annotations.update(base_.__annotations__)

        for field in annotations:
            annotation = annotations[field]
            origin = get_origin(annotation)
            if isclass(annotation) and issubclass(annotation, DjangoModel):
                annotations[field] = ForeignKey[annotation]
            elif isclass(origin) and issubclass(origin, QuerySet):
                annotations[field] = Annotated[
                    annotation,
                    Field(default_factory=get_type(annotation)._default_manager.none),
                ]
        namespaces["__annotations__"] = annotations
        return map_method_aliases(
            super().__new__(mcs, name, bases, namespaces, **kwargs)
        )


class BaseModel(PyDBaseModel, metaclass=BaseModelMeta):
    @model_validator(mode="before")
    @classmethod
    def build_cache(cls, data: Any) -> Any:
        from camomilla.structured.cache import CacheBuilder

        return CacheBuilder.from_model(cls).inject_cache(data)
