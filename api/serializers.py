from rest_framework import serializers
from .models import Article, Tag, Category, Content, Media, SitemapUrl

from hvad.contrib.restframework import TranslatableModelSerializer


class TagSerializer(TranslatableModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(TranslatableModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ContentSerializer(TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'


class ExpandendArticleSerializer(TranslatableModelSerializer):

    tags = serializers.SerializerMethodField('get_translated_tags')
    categories = serializers.SerializerMethodField('get_translated_categories')
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_translated_tags(self, obj):
        tags = obj.tags
        return TagSerializer(tags, many=True, language=self.language).data

    def get_translated_categories(self, obj):
        categories = obj.categories
        return CategorySerializer(categories, many=True, language=self.language).data


class SitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id','url',)
