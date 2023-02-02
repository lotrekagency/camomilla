from django.shortcuts import redirect
from django.urls import include, path
from rest_framework import routers

from camomilla.views import (
    ArticleViewSet,
    CamomillaAuthLogin,
    CamomillaAuthLogout,
    CamomillaObtainAuthToken,
    ContentViewSet,
    LanguageViewSet,
    MediaFolderViewSet,
    MediaViewSet,
    PageViewSet,
    PermissionViewSet,
    TagViewSet,
    UserViewSet,
    MenuViewSet
)

router = routers.DefaultRouter()

router.register(r"tags", TagViewSet, "camomilla-tags")
router.register(r"articles", ArticleViewSet, "camomilla-articles")
router.register(r"contents", ContentViewSet, "camomilla-content")
router.register(r"media", MediaViewSet, "camomilla-media")
router.register(r"media-folders", MediaFolderViewSet, "camomilla-media_folders")
router.register(r"pages", PageViewSet, "camomilla-pages")
router.register(r"sitemap", PageViewSet, "camomilla-sitemap")
router.register(r"users", UserViewSet, "camomilla-users")
router.register(r"permissions", PermissionViewSet, "camomilla-permissions")
router.register(r"menus", MenuViewSet, "camomilla-menus")

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
