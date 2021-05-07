from camomilla.views.mixins.pagination import PaginateStackMixin
from .mixins import GetUserLanguageMixin, TrashMixin
from rest_framework import viewsets

from ..models import Article
from ..serializers import ExpandedArticleSerializer, ArticleSerializer
from ..permissions import CamomillaBasePermissions


class ArticleViewSet(
    PaginateStackMixin, GetUserLanguageMixin, TrashMixin, viewsets.ModelViewSet
):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Article
