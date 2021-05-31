from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin
from ..models import Page
from ..serializers import PageSerializer
from ..permissions import CamomillaBasePermissions


class PageViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Page
