from ..models import Article, Category, Tag
from .base import BaseTranslatableModelSerializer


class TagSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
