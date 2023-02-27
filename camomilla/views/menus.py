from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response

from camomilla.models import AbstractPage, Menu
from camomilla.permissions import CamomillaBasePermissions
from camomilla.serializers import ContentTypeSerializer, MenuSerializer
from camomilla.views.base import BaseModelViewset


class MenuViewSet(BaseModelViewset):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Menu

    @action(detail=False, methods=["get"], url_path="page_types")
    def page_types(self, request, *args, **kwargs):
        return Response(
            ContentTypeSerializer(
                [
                    model
                    for model in ContentType.objects.all()
                    if model.model_class()
                    and issubclass(model.model_class(), AbstractPage)
                ],
                many=True,
            ).data
        )

    @action(detail=False, methods=["get"], url_path=r"page_types/(?P<content_id>\w+)")
    def page_type_instances(self, request, content_id, *args, **kwargs):
        content_type = ContentType.objects.filter(pk=content_id).first()
        if not content_type or not issubclass(content_type.model_class(), AbstractPage):
            raise Http404("No object matches the given query.")
        return Response(
            [
                {"id": obj.pk, "name": str(obj), "url_node_id": obj.url_node.pk}
                for obj in content_type.model_class().objects.exclude(url_node__isnull=True)
            ]
        )
