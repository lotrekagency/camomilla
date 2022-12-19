from .related import RelatedField
from .file import ImageField, FileField
from hvad.contrib.restframework import TranslatableModelSerializer
from hvad.models import TranslatableModel
from django.db import models
from rest_framework import serializers


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


class FieldsOverrideMixin:
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
        if field_class is RelatedField:
            field_kwargs["serializer"] = build_standard_model_serializer(
                relation_info[1]
            )
        return field_class, field_kwargs


class TranslatableFieldsOverrideMixin(FieldsOverrideMixin):

    serializer_field_mapping = {
        **TranslatableModelSerializer.serializer_field_mapping,
        models.FileField: FileField,
        models.ImageField: ImageField,
    }
