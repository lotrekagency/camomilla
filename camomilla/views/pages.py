from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..utils import get_camomilla_model
from ..serializers import PageSerializer
from ..permissions import CamomillaBasePermissions


class PageViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = get_camomilla_model("page").objects.all()
    serializer_class = PageSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = get_camomilla_model("page")
