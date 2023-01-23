from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin

from ..utils import get_camomilla_model
from ..serializers import ArticleSerializer
from ..permissions import CamomillaBasePermissions


class ArticleViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = get_camomilla_model("article").objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (CamomillaBasePermissions,)
    search_fields = ["title", "identifier", "content", "permalink"]
    model = get_camomilla_model("article")
