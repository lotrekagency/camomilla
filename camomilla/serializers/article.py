from ..models import Article, Category, Tag
from .base import BaseModelSerializer


class TagSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
