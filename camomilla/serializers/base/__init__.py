from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework import serializers

from ..fields import FieldsOverrideMixin, TranslatableFieldsOverrideMixin
from ..mixins import (
    JSONFieldPatchMixin,
    LangInfoMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
    TranslationSetMixin,
    NestMixin,
)


class BaseModelSerializer(
    NestMixin,
    FieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
    serializers.ModelSerializer,
):
    pass


class BaseTranslatableModelSerializer(
    NestMixin,
    TranslatableFieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    LangInfoMixin,
    TranslationSetMixin,
    TranslatableModelSerializer,
):
    pass
