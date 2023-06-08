from typing import Any
from .fields import *
from .models import *
from django.db.models import JSONField
from django.db.models.query_utils import DeferredAttribute


class StructuredDescriptior(DeferredAttribute):
    def __set__(self, instance, value):
        if isinstance(value, dict):
            value = self.field.schema(**value)
        value.validate()
        instance.__dict__[self.field.attname] = value


class StructuredJSONField(JSONField):
    # TODO: rewrite descriptor class to do always return a schema obj or null
    # TODO: share cache in querysets of models having this same field
    # TODO: write queries for prefetch related for models inside the field

    descriptor_class = StructuredDescriptior

    def __init__(self, schema, *args: Any, **kwargs: Any) -> None:
        self.schema = schema
        return super().__init__(*args, **kwargs)

    def from_db_value(self, *args, **kwargs):
        value = super().from_db_value(*args, **kwargs)
        return value and self.schema(**value)

    def get_prep_value(self, value):
        if not value:
            return super().get_prep_value(value)
        if not isinstance(value, self.schema):
            value = self.schema(**value)
        return super().get_prep_value(value.to_struct())

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["schema"] = self.schema
        return name, path, args, kwargs
