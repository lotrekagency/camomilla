from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..serializers import TagSerializer
from ..permissions import CamomillaBasePermissions
from ..utils import get_camomilla_model


class TagViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = get_camomilla_model("tag").objects.all()
    serializer_class = TagSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = get_camomilla_model("tag")
