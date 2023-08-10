from camomilla.models import Tag
from camomilla.permissions import CamomillaBasePermissions
from camomilla.serializers import TagSerializer
from camomilla.views.base import BaseModelViewset
from camomilla.views.mixins import BulkDeleteMixin, GetUserLanguageMixin


class TagViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Tag
