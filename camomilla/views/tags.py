from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..models import Tag
from ..serializers import TagSerializer
from ..permissions import CamomillaBasePermissions


class TagViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Tag
