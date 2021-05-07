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


class ExpandedArticleSerializer(
    TranslationsMixin, CamomillaBaseTranslatableModelSerializer
):

    tags = serializers.SerializerMethodField("get_translated_tags")
    categories = serializers.SerializerMethodField("get_translated_categories")
    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source="highlight_image", read_only=True)
    og_image_exp = MediaSerializer(source="og_image", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def get_translated_tags(self, obj):
        tags = (
            Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        )
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = (
            Category.objects.language(self.ulanguage)
            .fallbacks()
            .filter(article__pk=obj.pk)
        )
        return CategorySerializer(categories, many=True).data
