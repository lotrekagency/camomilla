from rest_framework.schemas.openapi import (
    SchemaGenerator as DRFSchemaGenerator,
    AutoSchema as DRFAutoSchema,
)
from camomilla.contrib.rest_framework.serializer import (
    TranslationsMixin,
    plain_to_nest,
    TRANS_ACCESSOR,
)


class AutoSchema(DRFAutoSchema):
    def map_serializer(self, serializer):
        schema = super(AutoSchema, self).map_serializer(serializer)
        if isinstance(serializer, TranslationsMixin) and serializer.is_translatable:
            schema = plain_to_nest(schema["properties"], serializer.translation_fields)
            schema[TRANS_ACCESSOR] = {
                "type": "object",
                "properties": {
                    k: {"type": "object", "properties": v}
                    for k, v in schema[TRANS_ACCESSOR].items()
                },
            }
        return schema


class SchemaGenerator(DRFSchemaGenerator):
    def create_view(self, callback, method, request=None):
        view = super(SchemaGenerator, self).create_view(callback, method, request)
        view.schema = AutoSchema()
        return view
