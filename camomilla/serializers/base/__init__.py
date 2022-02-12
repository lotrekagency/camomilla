from ..mixins import LangInfoMixin, SetupEagerLoadingMixin, TranslationSetMixin
from rest_framework import serializers
from hvad.contrib.restframework import TranslatableModelSerializer
from django.db import models
from ..fields import FileField, ImageField, RelatedField


class BaseModelSerializer(SetupEagerLoadingMixin, serializers.ModelSerializer):
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
    serializer_related_field = RelatedField


class BaseTranslatableModelSerializer(
    LangInfoMixin, TranslationSetMixin, TranslatableModelSerializer
):
    serializer_field_mapping = {
        **TranslatableModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
    serializer_related_field = RelatedField
