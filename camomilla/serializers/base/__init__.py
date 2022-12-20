from hvad.contrib.restframework import TranslatableModelSerializer
from hvad.models import TranslatableModel
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


def build_standard_model_serializer(self, model, depth):
    return type(
        f"{model.__name__}StandardSerializer",
        (
            BaseTranslatableModelSerializer
            if issubclass(model, TranslatableModel)
            else BaseModelSerializer,
        ),
        {
            "Meta": type(
                "Meta",
                (object,),
                {"model": model, "depth": depth, "fields": "__all__"},
            )
        },
    )


class BaseModelSerializer(
    NestMixin,
    FieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    SetupEagerLoadingMixin,
    serializers.ModelSerializer,
):

    build_standard_model_serializer = build_standard_model_serializer


class BaseTranslatableModelSerializer(
    NestMixin,
    TranslatableFieldsOverrideMixin,
    JSONFieldPatchMixin,
    OrderingMixin,
    LangInfoMixin,
    TranslationSetMixin,
    TranslatableModelSerializer,
):
    build_standard_model_serializer = build_standard_model_serializer
