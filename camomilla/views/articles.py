from .mixins import GetUserLanguageMixin, BulkDeleteMixin, PaginateStackMixin
from rest_framework import viewsets

from ..models import Article
from ..serializers import  ArticleSerializer
from ..permissions import CamomillaBasePermissions


class ArticleViewSet(PaginateStackMixin, GetUserLanguageMixin, BulkDeleteMixin, viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Article
