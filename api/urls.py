from .views import ArticleViewSet, LanguageViewSet, CategoryViewSet, TagViewSet

from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
