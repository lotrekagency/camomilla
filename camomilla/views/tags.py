from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..models import Tag
from ..serializers import TagSerializer
from ..permissions import CamomillaBasePermissions
from rest_framework import viewsets


class TagViewSet(GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Tag
