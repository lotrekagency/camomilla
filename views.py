import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics, mixins, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import detail_route, list_route


from .models import Article, Tag, Category, Content, Media, SitemapUrl
from .serializers import ExpandedArticleSerializer, ArticleSerializer, MediaSerializer
from .serializers import TagSerializer, CategorySerializer, ContentSerializer, UserProfileSerializer
from .serializers import SitemapUrlSerializer, CompactSitemapUrlSerializer, UserSerializer, PermissionSerializer
from .permissions import CamomillaBasePermissions, CamomillaSuperUser


class GetUserLanguageMixin(object):
    def _get_user_language(self):
        return self.request.GET.get(
            'language', self.request.data.get('language_code', settings.LANGUAGE_CODE)
        )


class CamomillaObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        try:
            return Response({'token': token.key})
        except:
            return Response({'token': token.key})


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    model = get_user_model()
    permission_classes = (CamomillaSuperUser,)

    @detail_route(methods=['post'])
    def kickout(self, request, pk=None):
        user = get_user_model().objects.get(pk=pk)
        try:
            user.auth_token.delete()
        except:
            pass

        return Response({})


class PermissionViewSet(viewsets.ModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    model = Permission
    permission_classes = (CamomillaSuperUser,)
    http_method_names = ['get', 'put', 'options', 'head']

    def get_queryset(self):
        permissions = Permission.objects.filter(
            Q(content_type__app_label__contains='camomilla') |
            Q(content_type__app_label__contains='plugin_') |
            Q(content_type__model='token') |
            Q(content_type__model='user')
        )
        return permissions


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    model = get_user_model()
    http_method_names = ['get', 'put', 'options', 'head']

    @list_route(methods=['get'])
    def me(self, request):
        personal_profile = request.user
        return Response(
            self.serializer_class(
                personal_profile,
                context={'request': request}
            ).data
        )


class ArticleViewSet(GetUserLanguageMixin, viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'permalink'
    permission_classes = (CamomillaBasePermissions,)
    model = Article
    serializers = {
        'compressed' : ArticleSerializer,
        'expanded' : ExpandedArticleSerializer
    }

    def get_dynamic_serializer(self, request):
        compressed = request.GET.get('compressed', False)
        current_serializer = self.serializers['expanded']
        if compressed:
            current_serializer = self.serializers['compressed']
        return current_serializer

    def list(self, request, *args, **kwargs):
        user_language = self._get_user_language()

        # Filter by status
        status = request.GET.get('status', None)
        # Filter by page
        page = request.GET.get('page', None)
        queryset = self.get_queryset()
        if status:
            queryset = queryset.filter(status=status)

        # Support pagination
        current_serializer = self.get_dynamic_serializer(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = current_serializer(
                page, many=True,
                ulanguage=user_language,
                context={'request': request}
            )
            return self.get_paginated_response(serializer.data)

        # Serialize
        serializer = current_serializer(
            queryset, many=True,
            ulanguage=user_language,
            context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_language = self._get_user_language()
        current_serializer = self.get_dynamic_serializer(request)
        try:
            instance = self.get_queryset().get(permalink=kwargs['permalink'])
        except Exception as ex:
            # In case you use a different permalink
            instance = self.model.objects.language('all').get(
                permalink=kwargs['permalink']
            )
            instance = self.get_queryset().get(master=instance.pk)
        serializer = current_serializer(
            instance, ulanguage=user_language,
            context={'request': request}
        )
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user_language = self._get_user_language()
        articles = self.model.objects.language(user_language).fallbacks().all()
        return articles


class ContentViewSet(GetUserLanguageMixin, viewsets.ModelViewSet):

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    model = Content
    lookup_field = 'identifier'
    permission_classes = (CamomillaBasePermissions,)

    def list(self, request, *args, **kwargs):
        user_language = self._get_user_language()
        status = request.GET.get('status', None)
        page = request.GET.get('page', None)

        queryset = self.get_queryset()
        if status:
            queryset = self.get_queryset().filter(status=status)
        if page:
            queryset = queryset.filter(page=page)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user_language = self._get_user_language()
        contents = self.model.objects.language(user_language).fallbacks().all()
        return contents


class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Tag

    def get_queryset(self):
        user_language = self.request.GET.get('language', settings.LANGUAGE_CODE)
        return self.model.objects.language(user_language).fallbacks().all()


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Category

    def get_queryset(self):
        user_language = self.request.GET.get('language', 'en')
        return self.model.objects.language(user_language).fallbacks().all()


class MediaViewSet(GetUserLanguageMixin, viewsets.ModelViewSet):

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    model = Media

    @list_route(methods=['post'], permission_classes = (CamomillaBasePermissions,))
    def upload(self, request):
        new_media = Media.objects.language(self._get_user_language()).create(
            title=request.POST['title'],
            alt_text=request.POST['alt_text'],
            file=request.FILES['file_contents'],
            name=request.POST['file_name'],
            size=0,
        )
        return redirect('media-detail', pk=new_media.pk)

    def _handle_upload_file(file):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def get_queryset(self):
        user_language = self._get_user_language()
        contents = self.model.objects.language(user_language).fallbacks().all()
        return contents


class SitemapUrlViewSet(GetUserLanguageMixin, viewsets.ModelViewSet):

    queryset = SitemapUrl.objects.all()
    serializer_class = SitemapUrlSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = SitemapUrl

    def get_serializer_class(self):
        if self.action == 'list':
            return CompactSitemapUrlSerializer
        return SitemapUrlSerializer

    def get_queryset(self):
        user_language = self._get_user_language()
        contents = self.model.objects.language(user_language).fallbacks().all()
        if request_get.get('permalink',''):
            queryset = queryset.filter(permlalink=request_get.get('permalink',''))
        return contents



class LanguageViewSet(views.APIView):

    def get(self, request, *args, **kwargs):

        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({
                'id' : key,
                'name' : language
            })
        return Response(languages)
