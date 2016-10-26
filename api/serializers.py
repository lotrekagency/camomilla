from rest_framework import serializers
from .models import Article, Language


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
