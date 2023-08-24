import inspect
from typing import Any, Dict, Tuple, get_args, get_origin
from typing_extensions import Annotated

import pydantic._internal._model_construction
from django.db.models import Model as DjangoModel
from pydantic import BaseModel as PyDBaseModel
from pydantic import Field
from .fields import ForeignKey, QuerySet


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
            origin = get_origin(annotations[field])
            if inspect.isclass(annotations[field]) and issubclass(
                annotations[field], DjangoModel
            ):
                annotations[field] = ForeignKey[annotations[field]]
            elif inspect.isclass(origin) and issubclass(origin, QuerySet):
                annotations[field] = Annotated[
                    annotations[field],
                    Field(default_factory=get_args(annotations[field])[0]._default_manager.none),
                ]

        namespaces["__annotations__"] = annotations
        return super().__new__(mcs, name, bases, namespaces, **kwargs)


class BaseModel(PyDBaseModel, metaclass=BaseModelMeta):
    pass
