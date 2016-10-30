import json

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import detail_route, list_route


from .models import Article, Language, Tag, Category, Content, Media, SitemapUrl
from .serializers import ExpandendArticleSerializer, ArticleSerializer, MediaSerializer
from .serializers import LanguageSerializer, TagSerializer, CategorySerializer, ContentSerializer
from .serializers import SitemapUrlSerializer, CompactSitemapUrlSerializer
from .permissions import IsSuperUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'permalink'

    def get_dynamic_serializer(self, request):
        compressed = request.GET.get('compressed', False)
        current_serializer = ExpandendArticleSerializer
        if compressed:
            current_serializer = ArticleSerializer
        return current_serializer

    def list(self, request, *args, **kwargs):

        status = request.GET.get('status', None)

        if status:
            queryset = Article.objects.filter(status=status)
        else:
            queryset = Article.objects.all()

        current_serializer = self.get_dynamic_serializer(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = current_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = current_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        current_serializer = self.get_dynamic_serializer(request)
        instance = self.get_object()
        serializer = current_serializer(instance)
        return Response(serializer.data)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'permalink'

    def list(self, request, *args, **kwargs):

        status = request.GET.get('status', None)

        if status:
            queryset = Content.objects.filter(status=status)
        else:
            queryset = Content.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ContentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ContentSerializer(queryset, many=True)
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


from django.http import HttpResponse

# LIMIT TO GET!!!!
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    @list_route(methods=['post'])
    def upload(self, request):
        Media.objects.create(
            file=request.FILES['file_contents'],
            name=request.POST['file_name'],
            dimension=0
        )
        return HttpResponse(status_code=200)

    def _handle_upload_file(file):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


class SitemapUrlViewSet(viewsets.ModelViewSet):
    queryset = SitemapUrl.objects.all()
    serializer_class = SitemapUrlSerializer

    @list_route(methods=['post'])
    def new(self, request):
        # DELETE ALL SITEMAPS
        urls = json.loads(request.POST['urls'])
        for url in urls:
            SitemapUrl.objects.create(url=url)
        return HttpResponse(status_code=200)

    def get_serializer_class(self):
        if self.action == 'list':
            return CompactSitemapUrlSerializer
        return SitemapUrlSerializer
