from .views import ArticleViewSet, CategoryViewSet
from .views import TagViewSet, ContentViewSet, MediaViewSet, SitemapUrlViewSet, LanguageViewSet

from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'media', MediaViewSet, 'media')
router.register(r'sitemap', SitemapUrlViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^languages/', LanguageViewSet.as_view())
]
