from .views import ArticleViewSet, CategoryViewSet
from .views import TagViewSet, ContentViewSet, MediaViewSet, SitemapUrlViewSet

from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'media', MediaViewSet)
router.register(r'sitemap', SitemapUrlViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
