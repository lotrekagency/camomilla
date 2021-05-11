from ..models import Article, Category, Tag
from .fields import RelatedField
from .media import MediaSerializer
from .mixins import CamomillaBaseTranslatableModelSerializer


class TagSerializer(CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(CamomillaBaseTranslatableModelSerializer):

    highlight_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    tags = RelatedField(serializer=TagSerializer, many=True, allow_null=True)
    og_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    
    class Meta:
        model = Article
        fields = "__all__"
