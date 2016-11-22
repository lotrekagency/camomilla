from rest_framework import serializers, permissions
from .models import Article, Tag, Category, Content, Media, SitemapUrl, UserProfile, Page

from hvad.contrib.restframework import TranslatableModelSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = '__all__'


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


class ContentSerializer(TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class MediaSerializer(TranslatableModelSerializer):

    class Meta:
        model = Media
        fields = '__all__'


#http://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers
class ArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ExpandendArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    tags = serializers.SerializerMethodField('get_translated_tags')
    categories = serializers.SerializerMethodField('get_translated_categories')
    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_translated_tags(self, obj):
        tags = Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = Category.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return CategorySerializer(categories, many=True).data


class SitemapUrlSerializer(TranslatableModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id','url',)
