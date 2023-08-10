from camomilla.models import Page
from camomilla.permissions import CamomillaBasePermissions
from camomilla.serializers import PageSerializer
from camomilla.views.base import BaseModelViewset
from camomilla.views.mixins import BulkDeleteMixin, GetUserLanguageMixin


class PageViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Page
