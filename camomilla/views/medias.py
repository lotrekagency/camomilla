from .base import BaseModelViewset
from .mixins import BulkDeleteMixin, GetUserLanguageMixin
from ..parsers import MultipartJsonParser
from django.shortcuts import redirect


from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import Media, MediaFolder
from ..serializers import MediaSerializer, MediaFolderSerializer, MediaListSerializer
from ..permissions import CamomillaBasePermissions


class MediaFolderViewSet(GetUserLanguageMixin, BaseModelViewset):
    model = MediaFolder
    serializer_class = MediaFolderSerializer
    items_per_page = 18

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_context(self):
        return {**super().get_serializer_context(), "action": "list"}

    def get_mixed_response(self, request, *args, **kwargs):
        updir = kwargs.get("pk", None)

        parent_folder = MediaFolderSerializer(
            self.model.objects.filter(pk=updir).first()
        ).data
        folder_queryset = self.model.objects.filter(updir__pk=updir)
        media_queryset = Media.objects.filter(folder__pk=updir)

        folder_data = MediaFolderSerializer(
            folder_queryset, many=True, context={"request": request}
        ).data
        media_data = self.format_output(
            *self.handle_pagination_stack(media_queryset),
            SerializerClass=MediaListSerializer
        )
        return {
            "folders": folder_data,
            "media": media_data,
            "parent_folder": parent_folder,
        }

    def list(self, request, *args, **kwargs):
        return Response(self.get_mixed_response(request, *args, **kwargs))

    def retrieve(self, request, *args, **kwargs):
        return Response(self.get_mixed_response(request, *args, **kwargs))


class MediaViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    model = Media
    parser_classes = [MultipartJsonParser]
