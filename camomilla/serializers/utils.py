def build_standard_model_serializer(model, depth, bases=None):
    if bases is None:
        from rest_framework.serializers import ModelSerializer
        from camomilla.serializers.fields import FieldsOverrideMixin
        from camomilla.serializers.mixins import (
            JSONFieldPatchMixin,
            NestMixin,
            OrderingMixin,
            SetupEagerLoadingMixin,
        )

        bases = (
            NestMixin,
            FieldsOverrideMixin,
            JSONFieldPatchMixin,
            OrderingMixin,
            SetupEagerLoadingMixin,
            ModelSerializer,
        )
    return type(
        f"{model.__name__}StandardSerializer",
        bases,
        {
            "Meta": type(
                "Meta",
                (object,),
                {"model": model, "depth": depth, "fields": "__all__"},
            )
        },
    )
