from rest_framework import serializers
from .models import Article, Language, Tag, Category, Content


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ExpandendArticleSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)
    language = LanguageSerializer()

    class Meta:
        model = Article
        fields = '__all__'
