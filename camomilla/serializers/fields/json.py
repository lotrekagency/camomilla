from rest_framework import serializers
from rest_framework.utils import model_meta

from camomilla.serializers.utils import build_standard_model_serializer
from camomilla.structured.fields import (
    EmbeddedField,
    ForeignKey,
    ForeignKeyList,
    ListField,
)
from camomilla.structured.models import Model


class StructuredJSONField(serializers.JSONField):
    def __init__(self, **kwargs):
        self.schema = kwargs.pop("schema", None)
        super().__init__(**kwargs)

    def bind(self, field_name, parent):
        if self.schema is None and isinstance(parent, serializers.ModelSerializer):
            info = model_meta.get_field_info(parent.Meta.model)
            field = info.fields[field_name]
            self.schema = field.schema
            self.many = field.many
        super().bind(field_name, parent)
    
    def to_json_schema(self):
        if self.many:
            return {
                'type': 'array',
                'items': self.schema.to_json_schema()
            }
        else:
            return self.schema.to_json_schema()

    def to_internal_value(self, data):
        if isinstance(data, dict):
            data = to_internal_model_value(self.schema, data)
        elif isinstance(data, list):
            data = [to_internal_model_value(self.schema, v) for v in data]
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(expanded_rapresentation(instance))


def expanded_model_rapresentation(schema: Model):
    stack = {}
    for _, name, field in schema.iterate_with_name():
        value = field.__get__(schema)
        if value is None:
            continue
        elif isinstance(field, ForeignKey):
            serializer = build_standard_model_serializer(field.model, depth=1)
            data = serializer(instance=value).data
        elif isinstance(field, ForeignKeyList):
            serializer = build_standard_model_serializer(field.inner_model, depth=1)
            data = serializer(instance=value, many=True).data
        elif isinstance(field, EmbeddedField):
            data = expanded_model_rapresentation(value)
        elif isinstance(field, ListField):
            data = []
            for v in value:
                if isinstance(v, Model):
                    v = expanded_model_rapresentation(v)
                data.append(v)
        else:
            data = field.to_struct(value)
        stack[name] = data
    return stack


def expanded_rapresentation(value):
    if isinstance(value, dict):
        value = {k: expanded_rapresentation(v) for k, v in value.items()}
    elif isinstance(value, list):
        value = [expanded_rapresentation(v) for v in value]
    elif isinstance(value, Model):
        value = expanded_model_rapresentation(value)
    return value


def to_internal_model_value(schema: Model, data):
    stack = {}
    for _, name, field in schema.iterate_with_name():
        value = data.get(name, None)
        if value is None:
            continue
        if isinstance(field, ForeignKey) and isinstance(value, dict):
            value = value.get(field.model._meta.pk.attname, None)
        elif isinstance(field, ForeignKeyList) and isinstance(value, list):
            attname = field.model._meta.pk.attname
            value = [v.get(attname, None) for v in value]
        elif isinstance(field, EmbeddedField):
            value = to_internal_model_value(field._get_embed_type(), value)
        elif isinstance(field, ListField):
            main_type = field._get_main_type()
            value = [to_internal_model_value(main_type, v) for v in value]
        else:
            value = field.to_struct(value)
        stack[name] = value
    return stack
