from ..mixins import (
    LangInfoMixin,
    SetupEagerLoadingMixin,
    TranslationSetMixin,
    OrderingMixin,
    JSONFieldPatchMixin,
)
from rest_framework import serializers
from hvad.contrib.restframework import TranslatableModelSerializer
from ..fields import FieldsOverrideMixin, TranslatableFieldsOverrideMixin


class BaseModelSerializer(
    FieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
    serializers.ModelSerializer,
):

    pass


class BaseTranslatableModelSerializer(
    TranslatableFieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    LangInfoMixin,
    TranslationSetMixin,
    TranslatableModelSerializer,
):
    pass
