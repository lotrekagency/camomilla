from .base import BaseModelViewset
from .mixins import BulkDeleteMixin, GetUserLanguageMixin
from ..parsers import MultipartJsonParser
from django.shortcuts import redirect


from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import Media, MediaFolder
from ..serializers import MediaSerializer, MediaFolderSerializer, MediaListSerializer
from ..permissions import CamomillaBasePermissions


class MediaFolderViewSet(
    GetUserLanguageMixin, BaseModelViewset
):
    model = MediaFolder
    serializer_class = MediaFolderSerializer
    items_per_page = 18

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_context(self):
        return {**super().get_serializer_context(), "action": "list"}

    def get_mixed_response(self, request, *args, **kwargs):
        updir = kwargs.get('pk', None)

        parent_folder = MediaFolderSerializer(self.model.objects.filter(pk=updir).first()).data
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

    @action(
        detail=False, methods=["post"], permission_classes=(CamomillaBasePermissions,)
    )
    def upload(self, request):
        if request.data and "file" in request.data:
            new_media = Media(
                # language_code=self._get_user_language(),
                title=request.data.get("title", ""),
                alt_text=request.data.get("alt_text", ""),
                name=request.data.get("file_name", ""),
                description=request.data.get("description", ""),
                folder=MediaFolder.objects.filter(
                    id=request.data.get("folder", "")
                ).first(),
                size=0,
            )
            upload = request.data["file"]

            new_media.file.save(upload.name, upload)
            new_media.save()
            serializer = MediaSerializer(new_media)
            return Response(serializer.data)
        else:
            new_media = Media.objects.language(self._get_user_language()).create(
                title=request.POST["title"],
                alt_text=request.POST["alt_text"],
                file=request.FILES["file_contents"],
                name=request.POST["file_name"],
                size=0,
            )

        return redirect("media-detail", pk=new_media.pk)

    def update(self, request, *args, **kwargs):
        partial = False
        if "PATCH" in request.method:
            partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
