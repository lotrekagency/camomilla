from hvad.contrib.restframework.serializers import TranslationsMixin
from rest_framework import serializers

from ..models import Article, Category, Tag
from .fields import RelatedField
from .media import MediaSerializer
from .mixins import CamomillaBaseTranslatableModelSerializer


class TagSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):

    highlight_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    tags = RelatedField(serializer=TagSerializer, many=True, allow_null=True)
    og_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    
    class Meta:
        model = Article
        fields = "__all__"

