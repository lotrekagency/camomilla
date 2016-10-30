from rest_framework import serializers
from .models import Article, Language, Tag, Category, Content, Media, SitemapUrl


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'


class ExpandendArticleSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)
    language = LanguageSerializer()
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class SitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id','url',)
