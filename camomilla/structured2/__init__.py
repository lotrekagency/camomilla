import json
from typing import Any

from django.db.models import JSONField
from django.db.models.query_utils import DeferredAttribute
from django_jsonform.models.fields import JSONFormField
from pydantic import TypeAdapter

from .fields import *
from .models import *


class StructuredJSONFormField(JSONFormField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encoder = kwargs.get("encoder", None)
        self.decoder = kwargs.get("decoder", None)


class StructuredEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, BaseModel):
            return z.model_dump_json(exclude_unset=True)
        else:
            return super().default(z)


class StructuredDescriptior(DeferredAttribute):
    field: "StructuredJSONField"

    def __set__(self, instance, value):
        if self.field.check_type(value):
            value = self.field.schema.validate_python(value)
        instance.__dict__[self.field.attname] = value


class StructuredJSONField(JSONField):
    # TODO: share cache in querysets of models having this same field
    # TODO: write queries for prefetch related for models inside the field

    descriptor_class = StructuredDescriptior

    def __init__(self, schema: type[BaseModel], *args: Any, **kwargs: Any) -> None:
        self.orig_schema = schema
        self.schema = schema
        default = kwargs.get("default", dict)
        self.file_handler = kwargs.pop("file_handler", "")
        self.many = kwargs.pop(
            "many", isinstance(default() if callable(default) else default, list)
        )
        if self.many:
            self.schema = TypeAdapter(list[self.schema])
        kwargs["encoder"] = kwargs.get("encoder", StructuredEncoder)
        return super().__init__(*args, **kwargs)

    def check_type(self, value: Any):
        if self.many:
            return isinstance(value, list) and all(
                True for v in value if isinstance(v, self.orig_schema)
            )
        return isinstance(value, self.orig_schema)

    def get_prep_value(self, value):
        return value.model_dump_json(exclude_unset=True)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["schema"] = self.schema
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": StructuredJSONFormField,
                "schema": self.schema.model_json_schema(),
                "model_name": self.model.__name__,
                "file_handler": self.file_handler,
                **kwargs,
            }
        )
