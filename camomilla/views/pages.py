from .mixins import GetUserLanguageMixin, BulkDeleteMixin, PaginateStackMixin
from ..models import Page
from ..serializers import PageSerializer
from ..permissions import CamomillaBasePermissions
from rest_framework import viewsets


class PageViewSet(PaginateStackMixin, GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Page
