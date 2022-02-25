from .base import BaseModelViewset
from .mixins import BulkDeleteMixin, GetUserLanguageMixin, TrigramSearchMixin
from ..parsers import MultipartJsonParser
from ..permissions import CamomillaBasePermissions


from rest_framework.response import Response

from ..models import Media, MediaFolder
from ..serializers import MediaSerializer, MediaFolderSerializer, MediaListSerializer


class ParseMimeMixin(object):
    def parse_filter(self, filter):
        filter_name, value = filter.split("=")
        if filter_name == "mime_type":
            if value == "*/*":
                return "mime_type__isnull", False
            elif value.endswith("/*"):
                return "mime_type__startswith", value.split("/")[0]
        return filter_name, super().parse_qs_value(value)


class MediaFolderViewSet(
    GetUserLanguageMixin, ParseMimeMixin, TrigramSearchMixin, BaseModelViewset
):
    model = MediaFolder
    serializer_class = MediaFolderSerializer
    permission_classes = (CamomillaBasePermissions,)
    items_per_page = 18
    search_fields = ["name", "title", "alt_text"]

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
        media_queryset = (
            Media.objects.language(self.active_language)
            if request.GET.get("search", None)
            else Media.objects.all()
        ).filter(folder__pk=updir)

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


class MediaViewSet(
    GetUserLanguageMixin,
    BulkDeleteMixin,
    ParseMimeMixin,
    TrigramSearchMixin,
    BaseModelViewset,
):

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Media
    parser_classes = [MultipartJsonParser]
