from .mixins import GetUserLanguageMixin, BulkDeleteMixin, PaginateStackMixin
from ..models import Category
from ..serializers import CategorySerializer
from ..permissions import CamomillaBasePermissions
from rest_framework import viewsets


class CategoryViewSet(PaginateStackMixin, GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Category