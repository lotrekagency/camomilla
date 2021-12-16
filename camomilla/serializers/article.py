from ..models import Article, Category, Tag
from .fields import RelatedField
from .media import MediaSerializer
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

    highlight_image = RelatedField(
        serializer=MediaSerializer, required=False, allow_null=True
    )
    tags = RelatedField(
        serializer=TagSerializer, many=True, required=False, allow_null=True
    )
    og_image = RelatedField(serializer=MediaSerializer, required=False, allow_null=True)

    class Meta:
        model = Article
        fields = "__all__"
