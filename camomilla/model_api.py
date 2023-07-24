from rest_framework import routers

from django.urls import path, include
from camomilla.views.base import BaseModelViewset
from camomilla.serializers.base import BaseModelSerializer

router = routers.DefaultRouter()
urlpatterns = []


def register(
    base_serializer=BaseModelSerializer,
    base_viewset=BaseModelViewset,
    serializer_meta={},
    viewset_attrs={},
    filters = None
):
    """
    Register a model to the API.
    :param base_serializer: The base serializer to use for the model.
    :param base_viewset: The base viewset to use for the model.
    :param serializer_meta: The meta class to use for the serializer.
    :param viewset_attrs: The attributes to add to the viewset.
    :param filters: The filters to apply to the queryset.
    :return: The model.
    """

    def inner(model):
        base_meta = {
            "model": model,
            "fields": "__all__",
        }
        if 'exclude' in serializer_meta:
            base_meta.pop('fields')
        serializer = type(
            f"{model.__name__}Serializer",
            (base_serializer,),
            {
                "Meta": type(
                    "Meta",
                    (),
                    {
                        **base_meta,
                        **serializer_meta,
                    },
                )
            },
        )

        viewset = type(
            f"{model.__name__}ViewSet",
            (base_viewset,),
            {
                "get_queryset": lambda self: model.objects.all() if filters is None else model.objects.filter(**filters),
                "serializer_class": serializer,
                **viewset_attrs,
            },
        )

        model_path = "".join(
            [
                "-" + character.lower()
                if character.isupper() and index > 0
                else character
                for index, character in enumerate(model.__name__)
            ]
        ).lstrip("-")

        router.register(
            f"{model_path.replace(' ', '_').lower().lower()}",
            viewset,
            f"{model.__name__.lower()}_api",
        )
        urlpatterns.append(path("", include(router.urls)))
        return model

    return inner
