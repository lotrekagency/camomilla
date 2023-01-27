from ..models import Article, Tag
from .base import BaseModelSerializer


class TagSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
