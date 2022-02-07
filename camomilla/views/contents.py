from .base import BaseModelViewset
import json

from django.http import JsonResponse
from django.utils.translation import get_language
from rest_framework.decorators import action

from ..models import Content
from ..permissions import CamomillaBasePermissions
from ..serializers import ContentSerializer
from .mixins import BulkDeleteMixin, GetUserLanguageMixin


class ContentViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    model = Content
    permission_classes = (CamomillaBasePermissions,)

    @action(detail=True, methods=["get", "patch"])
    def djsuperadmin(self, request, pk):
        # content, _ = Content.objects.get_or_create(pk=pk)
        # content.translate(get_language())
        try:
            content = Content.objects.language(get_language()).get(pk=pk)
        except Content.DoesNotExist:
            content, _ = Content.objects.get_or_create(pk=pk)
            content.translate(get_language())
        if request.method == "GET":
            return JsonResponse({"content": content.content})
        if request.method == "PATCH":
            data = json.loads(request.body)
            content_data = data["content"]
            content.content = content_data
            content.save()
            return JsonResponse({"content": content_data})
