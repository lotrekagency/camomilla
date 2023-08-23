from collections import defaultdict
from typing import Any

from django_jsonform.models.fields import JSONFormField

from django.db.models import JSONField
from django.db.models.query_utils import DeferredAttribute

from camomilla.utils.getters import find_and_replace_dict

from .fields import *
from .models import *
from .models import _Cache, build_model_cache
import json


class StructuredJSONFormField(JSONFormField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encoder = kwargs.get("encoder", None)
        self.decoder = kwargs.get("decoder", None)


class StructuredEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, models.Model):
            return z.to_struct()
        else:
            return super().default(z)


class StructuredDescriptior(DeferredAttribute):
    def __set__(self, instance, value):
        if isinstance(value, dict):
            self.field.prefetch_related(value)
            value = self.field.populate_schema(value)
        elif isinstance(value, list):
            self.field.prefetch_related(value)
            _stack = []
            for v in value:
                if isinstance(v, dict):
                    v = self.field.populate_schema(v)
                elif not isinstance(v, self.field.schema):
                    raise TypeError(
                        f"{type(v)} is not a valid type for the given schema ({self.field.schema})."
                    )
                v.validate()
                _stack.append(v)
            value = _stack
        elif isinstance(value, self.field.schema):
            value.validate()
        else:
            raise TypeError(
                f"{type(value)} is not a valid type for the given schema ({self.field.schema})."
            )
        instance.__dict__[self.field.attname] = value


class StructuredJSONField(JSONField):
    # TODO: share cache in querysets of models having this same field
    # TODO: write queries for prefetch related for models inside the field

    descriptor_class = StructuredDescriptior

    def __init__(self, schema, *args: Any, **kwargs: Any) -> None:
        self.schema = schema
        default = kwargs.get("default", dict)
        self.file_handler = kwargs.pop("file_handler", "")
        self.many = kwargs.pop(
            "many", isinstance(default() if callable(default) else default, list)
        )
        kwargs["encoder"] = kwargs.get("encoder", StructuredEncoder)
        self._cache = _Cache(self)
        return super().__init__(*args, **kwargs)

    def populate_schema(self, struct):
        schema_intance = self.schema()
        relations = schema_intance.prepopulate(**struct)
        schema_intance.bind(self)
        schema_intance.populate(**relations)
        return schema_intance

    def get_prep_value(self, value):
        if not value:
            return super().get_prep_value(value)
        if isinstance(value, list):
            value = [
                (v if isinstance(v, self.schema) else self.populate_schema(v))
                for v in value
            ]
            value = [self.schema.to_db_transform(v.to_struct()) for v in value]
        elif isinstance(value, dict):
            value = self.schema.to_db_transform(self.populate_schema(value).to_struct())
        elif isinstance(value, self.schema):
            value = self.schema.to_db_transform(value.to_struct())
        else:
            raise TypeError(f"{type(value)} is not a valid type for the given schema.")
        return super().get_prep_value(value)

    def from_db_value(self, value, expression, connection):
        return self.schema.from_db_transform(
            super().from_db_value(value, expression, connection)
        )

    def get_prefetched_data(self):
        return self._cache.get_prefetched_data()

    def get_all_relateds(self, struct):
        if isinstance(struct, list):
            relateds = defaultdict(set)
            for inner_struct in struct:
                if isinstance(inner_struct, dict):
                    child_relateds = self.schema.get_all_relateds(inner_struct)
                    for model, pks in child_relateds.items():
                        relateds[model].update(pks)
            return relateds
        return self.schema.get_all_relateds(struct)

    def prefetch_related(self, struct):
        relateds = self.get_all_relateds(struct)
        for model, pks in relateds.items():
            self._cache.prefetched_data[model] = (
                {obj.pk: obj for obj in build_model_cache(model, pks)}
                if len(pks) > 0
                else {}
            )

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["schema"] = self.schema
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        json_schema = self.to_json_schema()

        def replace(key, value):
            if (
                key != "$ref"
                and isinstance(value, str)
                and value.startswith("#/definitions")
            ):
                return {"$ref": value}
            elif isinstance(value, dict) and value.get("type", None) == "object":
                if not bool(
                    set(("properties", "keys", "oneOf", "anyOf", "allOf"))
                    & set(value.keys())
                ):
                    value["keys"] = {}
            return value

        return super().formfield(
            **{
                "form_class": StructuredJSONFormField,
                "schema": find_and_replace_dict(json_schema, replace),
                "model_name": self.model.__name__,
                "file_handler": self.file_handler,
                **kwargs,
            }
        )

    def to_json_schema(self):
        json_schema = self.schema.to_json_schema()
        definitions = json_schema.pop("definitions", None)
        if self.many:
            return {
                "type": "array",
                "items": json_schema,
                **({"definitions": definitions} if definitions else {}),
            }
        else:
            return {
                **json_schema,
                **({"definitions": definitions} if definitions else {}),
            }
