import json

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import detail_route, list_route


from .models import Article, Tag, Category, Content, Media, SitemapUrl, UserProfile
from .serializers import ExpandendArticleSerializer, ArticleSerializer, MediaSerializer
from .serializers import TagSerializer, CategorySerializer, ContentSerializer
from .serializers import SitemapUrlSerializer, CompactSitemapUrlSerializer
from .permissions import IsSuperUserOrReadOnly


class CamomillaObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        try:
            return Response(
                {
                    'token': token.key,
                    'user': {
                        'level' : user.userprofile.level,
                        'profile_image' : '',
                    }
                }
            )
        except UserProfile.DoesNotExist:
            return Response({'token': token.key})


from hvad.utils import get_translation_aware_manager

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
        user_language = self._get_user_language()
        status = request.GET.get('status', None)

        if status:
            queryset = self.get_queryset().filter(status=status)
        else:
            queryset = self.get_queryset()

        current_serializer = self.get_dynamic_serializer(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = current_serializer(page, many=True, language=user_language)
            return self.get_paginated_response(serializer.data)

        serializer = current_serializer(queryset, many=True, language=user_language)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        current_serializer = self.get_dynamic_serializer(request)
        instance = self.get_object()
        serializer = current_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def _get_user_language(self):
        return self.request.GET.get('language', 'en')

    def get_queryset(self):
        user_language = self._get_user_language()
        articles = Article.objects.language(user_language).fallbacks().all()
        for article in articles:
            article.tags = article.tags.language(user_language).fallbacks().all()
        return articles


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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user_language = self.request.GET.get('language', 'en')
        return Content.objects.language(user_language).fallbacks().all()


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        user_language = self.request.GET.get('language', 'en')
        return Tag.objects.language(user_language).fallbacks().all()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        user_language = self.request.GET.get('language', 'en')
        return Category.objects.language(user_language).fallbacks().all()


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
        SitemapUrl.objects.all().delete()
        urls = json.loads(request.POST['urls'])
        for url in urls:
            SitemapUrl.objects.create(url=url)
        return HttpResponse(status_code=200)

    def get_serializer_class(self):
        if self.action == 'list':
            return CompactSitemapUrlSerializer
        return SitemapUrlSerializer
