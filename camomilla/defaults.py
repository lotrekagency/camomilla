import os

from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = []
if os.path.exists(os.path.join(BASE_DIR, "build")):
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, "build"))
if os.path.exists(os.path.join(BASE_DIR, "public")):
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, "public"))

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

THUMB_FOLDER = "thumbnails"

REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication"
        "camomilla.authentication.SessionAuthentication"
    ),
}

ADMIN_SITE_HEADER = _("Camomilla advanced panel")

CAMOMILLA_THUMBNAIL_WIDTH = 50
CAMOMILLA_THUMBNAIL_HEIGHT = 50


PNG_OPTIMIZATION_COMMAND = "pngquant {0} -f --ext .png"
JPEG_OPTIMIZATION_COMMAND = "jpegoptim {0}"

LANG_ON_PREFERENCE_DISABLED_VIEWS = ["sitemap", "sitemap_xml"]

HVAD = {"AUTOLOAD_TRANSLATIONS": True}
