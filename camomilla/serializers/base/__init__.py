from rest_framework import serializers

from ...contrib.rest_framework.serializer import TranslationsMixin
from ..fields import FieldsOverrideMixin
from ..mixins import (
    JSONFieldPatchMixin,
    LangInfoMixin,
    NestMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
)


class BaseModelSerializer(
    NestMixin,
    FieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
    TranslationsMixin,
    serializers.ModelSerializer,
):
    pass
