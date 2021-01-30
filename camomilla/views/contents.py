from django.http import JsonResponse
from django.utils.translation import get_language

import json
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import Content
from ..serializers import ContentSerializer
from ..permissions import CamomillaBasePermissions
from .mixins import GetUserLanguageMixin, BulkDeleteMixin


class ContentViewSet(GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    model = Content
    permission_classes = (CamomillaBasePermissions,)

    def list(self, request, *args, **kwargs):
        user_language = self._get_user_language()
        status = request.GET.get("status", None)
        page = request.GET.get("page", None)

        queryset = self.get_queryset()
        if status:
            queryset = self.get_queryset().filter(status=status)
        if page:
            queryset = queryset.filter(page=page)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

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
