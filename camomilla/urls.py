from .views import (
    ArticleViewSet,
    CamomillaObtainAuthToken,
    CamomillaAuthLogout,
    CamomillaAuthLogin,
    CategoryViewSet,
    MediaFolderViewSet,
)
from .views import TagViewSet, ContentViewSet, MediaViewSet, PermissionViewSet
from .views import PageViewSet, LanguageViewSet, UserViewSet

from django.urls import include, path
from django.shortcuts import redirect

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"tags", TagViewSet, "camomilla-tags")
router.register(r"categories", CategoryViewSet, "camomilla-categories")
router.register(r"articles", ArticleViewSet, "camomilla-articles")
router.register(r"contents", ContentViewSet, "camomilla-content")
router.register(r"media", MediaViewSet, "camomilla-media")
router.register(r"media-folders", MediaFolderViewSet, "camomilla-media_folders")
router.register(r"pages", PageViewSet, "camomilla-pages")
router.register(r"sitemap", PageViewSet, "camomilla-sitemap")
router.register(r"users", UserViewSet, "camomilla-users")
router.register(r"permissions", PermissionViewSet, "camomilla-permissions")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "profiles/me/", lambda _: redirect("../../users/current/"), name="profiles-me"
    ),
    path("token-auth/", CamomillaObtainAuthToken.as_view(), name="api_token"),
    path("auth/login/", CamomillaAuthLogin.as_view(), name="login"),
    path("auth/logout/", CamomillaAuthLogout.as_view(), name="logout"),
    path("languages/", LanguageViewSet.as_view(), name="get_languages"),
]
