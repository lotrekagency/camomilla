from django.db import models
from rest_framework import serializers

from camomilla import structured

from .json import StructuredJSONField
from .file import FileField, ImageField
from .related import RelatedField


class FieldsOverrideMixin:
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
        structured.StructuredJSONField: StructuredJSONField,
    }
    serializer_related_field = RelatedField
