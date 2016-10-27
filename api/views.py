from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route


from .models import Article, Language, Tag, Category
from .serializers import ExpandendArticleSerializer, ArticleSerializer
from .serializers import LanguageSerializer, TagSerializer, CategorySerializer
from .permissions import IsSuperUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):

        status = request.GET.get('status', None)
        if status:
            queryset = Article.objects.filter(status=status)
        else:
            queryset = Article.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ExpandendArticleSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ExpandendArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ExpandendArticleSerializer(instance)
        return Response(serializer.data)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
