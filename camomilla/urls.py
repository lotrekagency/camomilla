from .views import (
    ArticleViewSet,
    CamomillaObtainAuthToken,
    CategoryViewSet,
    MediaFolderViewSet,
)
from .views import TagViewSet, ContentViewSet, MediaViewSet, PermissionViewSet
from .views import PageViewSet, LanguageViewSet, UserProfileViewSet, UserViewSet

from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"tags", TagViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"articles", ArticleViewSet)
router.register(r"contents", ContentViewSet)
router.register(r"media", MediaViewSet, "media")
router.register(r"media-folders", MediaFolderViewSet, "media_folders")
router.register(r"pages", PageViewSet)
router.register(r"sitemap", PageViewSet)
router.register(r"profiles", UserProfileViewSet)
router.register(r"users", UserViewSet)
router.register(r"permissions", PermissionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("token-auth/", CamomillaObtainAuthToken.as_view(), name="api_token"),
    path("languages/", LanguageViewSet.as_view(), name="get_languages"),
]
