from rest_framework import serializers
from rest_framework.utils import model_meta


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
            self.json_schema = field.schema.json_schema()
        super().bind(field_name, parent)

    def to_representation(self, instance):
        if isinstance(instance, list) and self.many:
            return super().to_representation(
                self.schema.dump_python(instance, exclude_unset=True)
            )
        return super().to_representation(instance.model_dump(exclude_unset=True))
