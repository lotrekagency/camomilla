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


class UnderTranslateMixin(object):

    def __init__(self, *args, **kwargs):
        self.ulanguage = 'en'
        try:
            self.ulanguage = kwargs.pop('ulanguage')
        except KeyError:
            pass
        super(UnderTranslateMixin, self).__init__(*args, **kwargs)


class ArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

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


class ExpandendArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    tags = serializers.SerializerMethodField('get_translated_tags')
    categories = serializers.SerializerMethodField('get_translated_categories')
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_translated_tags(self, obj):
        tags = Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = Category.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return CategorySerializer(categories, many=True).data


class SitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id','url',)
