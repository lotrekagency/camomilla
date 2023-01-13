from .related import RelatedField
from .file import ImageField, FileField
from django.db import models
from rest_framework import serializers


class FieldsOverrideMixin:
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
    serializer_related_field = RelatedField
