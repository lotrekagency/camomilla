from .views import ArticleViewSet, LanguageViewSet

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'languages', ArticleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
