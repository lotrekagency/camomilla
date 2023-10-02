from rest_framework import serializers

from ...contrib.rest_framework.serializer import TranslationsMixin
from ..fields import FieldsOverrideMixin
from ..mixins import (
    JSONFieldPatchMixin,
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
    """
    This is the base serializer for all the models.
    It adds support for:
    - nesting translations fields under a "translations" field
    - overriding related fields with auto-generated serializers
    - patching JSONField
    - ordering
    - eager loading
    """

    pass


__all__ = [
    "BaseModelSerializer",
]
