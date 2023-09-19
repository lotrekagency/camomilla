import json
from typing import Any, Union, TYPE_CHECKING

from django.db.models import JSONField
from django.db.models.query_utils import DeferredAttribute
from django_jsonform.models.fields import JSONFormField
from pydantic import (
    TypeAdapter,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    WrapValidator,
)

from .fields import *
from .models import *

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pydantic.fields import Field
    from typing_extensions import Annotated


class StructuredJSONFormField(JSONFormField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encoder = kwargs.get("encoder", None)
        self.decoder = kwargs.get("decoder", None)

    def prepare_value(self, value):
        if isinstance(value, list):
            return json.dumps([v.model_dump() for v in value])
        return value.model_dump_json()


class StructuredDescriptior(DeferredAttribute):
    field: "StructuredJSONField"

    def __set__(self, instance, value):
        # TODO: check if it's better to validate here or in __get__ function (performance reasons)
        # if not self.field.check_type(value):
        #     value = self.field.schema.validate_python(value)
        instance.__dict__[self.field.attname] = value

    def __get__(self, instance, cls=None):
        value = super().__get__(instance, cls)
        if not self.field.check_type(value):
            return self.field.schema.validate_python(value)
        return value


class StructuredJSONField(JSONField):
    # TODO: share cache in querysets of models having this same field
    # TODO: write queries for prefetch related for models inside the field

    descriptor_class = StructuredDescriptior

    @property
    def list_data_validator(self):
        def list_data_validator(
            value: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
        ) -> Any:
            from camomilla.structured.cache import CacheBuilder

            cache = CacheBuilder.from_model(self.orig_schema)
            if info.mode == "json" and isinstance(value, str):
                return self.schema.validate_python(
                    cache.inject_cache(json.loads(value))
                )
            return handler(cache.inject_cache(value))

        return list_data_validator

    def __init__(self, schema: type[BaseModel], *args: Any, **kwargs: Any) -> None:
        self.orig_schema = schema
        self.schema = schema
        default = kwargs.get("default", dict)
        self.file_handler = kwargs.pop("file_handler", "")
        self.many = kwargs.pop(
            "many", isinstance(default() if callable(default) else default, list)
        )
        if self.many:
            self.schema = TypeAdapter(
                Annotated[
                    list[self.schema],
                    Field(default_factory=list),
                    WrapValidator(self.list_data_validator),
                ]
            )
        return super().__init__(*args, **kwargs)

    def check_type(self, value: Any):
        if self.many:
            return isinstance(value, list) and all(
                isinstance(v, self.orig_schema) for v in value
            )
        return isinstance(value, self.orig_schema)

    def get_prep_value(
        self, value: Union[list[type[BaseModel]], type[BaseModel]]
    ) -> str:
        if isinstance(value, list) and self.many:
            return self.schema.dump_json(value, exclude_unset=True).decode()
        return value.model_dump_json(exclude_unset=True)

    def from_db_value(self, value: Any, expression: Any, connection: Any) -> Any:
        data = super().from_db_value(value, expression, connection)
        if isinstance(data, str):
            return json.loads(data)
        return data

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["schema"] = self.orig_schema
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": StructuredJSONFormField,
                "schema": self.schema.json_schema(),
                "model_name": self.model.__name__,
                "file_handler": self.file_handler,
                **kwargs,
            }
        )
