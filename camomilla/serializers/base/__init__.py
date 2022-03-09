from ..mixins import (
    LangInfoMixin,
    SetupEagerLoadingMixin,
    TranslationSetMixin,
    OrderingMixin,
)
from rest_framework import serializers
from hvad.contrib.restframework import TranslatableModelSerializer
from django.db import models
from ..fields import FileField, ImageField, RelatedField
from hvad.models import TranslatableModel


def build_standard_model_serializer(model):
    return type(
        f"{model.__name__}StandardSerializer",
        (
            TranslatableModelSerializer
            if issubclass(model, TranslatableModel)
            else serializers.ModelSerializer,
        ),
        {"Meta": type("Meta", (object,), {"model": model, "fields": "__all__"})},
    )


class BaseModelSerializer(
    OrderingMixin, SetupEagerLoadingMixin, serializers.ModelSerializer
):
    serializer_field_mapping = {
        **serializers.ModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
    serializer_related_field = RelatedField

    def build_relational_field(self, field_name, relation_info):
        field_class, field_kwargs = super().build_relational_field(
            field_name, relation_info
        )
        field_kwargs["serializer"] = build_standard_model_serializer(relation_info[1])
        return field_class, field_kwargs


class BaseTranslatableModelSerializer(
    OrderingMixin, LangInfoMixin, TranslationSetMixin, TranslatableModelSerializer
):
    serializer_field_mapping = {
        **TranslatableModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
    serializer_related_field = RelatedField

    def build_relational_field(self, field_name, relation_info):
        field_class, field_kwargs = super().build_relational_field(
            field_name, relation_info
        )
        field_kwargs["serializer"] = build_standard_model_serializer(relation_info[1])
        return field_class, field_kwargs
