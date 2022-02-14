from .base import BaseModelViewset
from .mixins import GetUserLanguageMixin, BulkDeleteMixin

from ..models import Article
from ..serializers import ArticleSerializer
from ..permissions import CamomillaBasePermissions


class ArticleViewSet(GetUserLanguageMixin, BulkDeleteMixin, BaseModelViewset):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (CamomillaBasePermissions,)
    search_fields = ["title", "identifier", "content", "permalink"]
    model = Article
