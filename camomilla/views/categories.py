from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..utils import get_camomilla_model
from ..serializers import CategorySerializer
from ..permissions import CamomillaBasePermissions


class CategoryViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = get_camomilla_model("category").objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CamomillaBasePermissions,)
    model = get_camomilla_model("category")
