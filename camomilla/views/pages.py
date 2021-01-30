from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..models import Page
from ..serializers import PageSerializer
from ..permissions import CamomillaBasePermissions
from ..serializers import CompactPageSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PageViewSet(GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Page

    def get_serializer_class(self):
        if self.action == "list":
            return CompactPageSerializer
        return PageSerializer

    def list(self, request, *args, **kwargs):
        user_language = self._get_user_language()
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_language = self._get_user_language()

        instance = self.get_queryset().get(pk=kwargs["pk"])
        serializer = self.serializer_class(instance, ulanguage=user_language)
        return Response(serializer.data)

    def get_queryset(self):
        user_language = self._get_user_language()
        contents = self.model.objects.language(user_language).fallbacks().all()
        request_get = self.request.GET
        if request_get.get("permalink", ""):
            contents = contents.filter(permalink=request_get.get("permalink", ""))
        return contents
