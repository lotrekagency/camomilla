from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route


from .models import Article, Language
from .serializers import ArticleSerializer, LanguageSerializer
from .permissions import IsSuperUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (IsSuperUserOrReadOnly,)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = LanguageSerializer
