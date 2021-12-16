from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..models import Category
from ..serializers import CategorySerializer
from ..permissions import CamomillaBasePermissions


class CategoryViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Category
