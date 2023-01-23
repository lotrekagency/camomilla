from .base import BaseModelViewset
import json

from django.http import JsonResponse
from django.utils.translation import get_language
from rest_framework.decorators import action

from ..utils import get_camomilla_model
from ..permissions import CamomillaBasePermissions
from ..serializers import ContentSerializer
from .mixins import BulkDeleteMixin, GetUserLanguageMixin


class ContentViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = get_camomilla_model("content").objects.all()
    serializer_class = ContentSerializer
    model = get_camomilla_model("content")
    permission_classes = (CamomillaBasePermissions,)

    @action(detail=True, methods=["get", "patch"])
    def djsuperadmin(self, request, pk):
        # content, _ = get_camomilla_model("content").objects.get_or_create(pk=pk)
        # content.translate(get_language())
        try:
            content = self.model.objects.language(get_language()).get(pk=pk)
        except self.model.DoesNotExist:
            content, _ = self.model.objects.get_or_create(pk=pk)
            content.translate(get_language())
        if request.method == "GET":
            return JsonResponse({"content": content.content})
        if request.method == "PATCH":
            data = json.loads(request.body)
            content_data = data["content"]
            content.content = content_data
            content.save()
            return JsonResponse({"content": content_data})
