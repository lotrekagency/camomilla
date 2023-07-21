from django.conf import settings as dj_settings
from camomilla.utils.getters import pointed_getter
from modeltranslation.settings import ENABLE_REGISTRATIONS


PROJECT_TITLE = pointed_getter(
    dj_settings,
    "CAMOMILLA.PROJECT_TITLE",
    pointed_getter(dj_settings, "CAMOMILLA_PROJECT_TITLE", "Camomilla"),
)

THUMBNAIL_FOLDER = pointed_getter(
    dj_settings,
    "CAMOMILLA.MEDIA.THUMBNAIL.FOLDER",
    pointed_getter(dj_settings, "CAMOMILLA_THUMBTHUMBNAIL_FOLDER", "thumbnails"),
)
THUMBNAIL_WIDTH = pointed_getter(
    dj_settings,
    "CAMOMILLA.MEDIA.THUMBNAIL.WIDTH",
    pointed_getter(dj_settings, "CAMOMILLA_THUMBNAIL_WIDTH", 50),
)
THUMBNAIL_HEIGHT = pointed_getter(
    dj_settings,
    "CAMOMILLA.MEDIA.THUMBNAIL.HEIGHT",
    pointed_getter(dj_settings, "CAMOMILLA_THUMBNAIL_HEIGHT", 50),
)
BASE_URL = pointed_getter(
    dj_settings,
    "CAMOMILLA.ROUTER.BASE_URL",
    pointed_getter(dj_settings, "FORCE_SCRIPT_NAME", None),
)
BASE_URL = BASE_URL and "/" + BASE_URL.strip("/")


ARTICLE_DEFAULT_TEMPLATE = pointed_getter(
    dj_settings, "CAMOMILLA.RENDER.ARTICLE.DEFAULT_TEMPLATE", "defaults/articles/default.html"
)
PAGE_DEFAULT_TEMPLATE = pointed_getter(
    dj_settings, "CAMOMILLA.RENDER.PAGE.DEFAULT_TEMPLATE", "defaults/pages/default.html"
)
ARTICLE_INJECT_CONTEXT_FUNC = pointed_getter(
    dj_settings, "CAMOMILLA.RENDER.ARTICLE.INJECT_CONTEXT", None
)
PAGE_INJECT_CONTEXT_FUNC = pointed_getter(
    dj_settings, "CAMOMILLA.RENDER.PAGE.INJECT_CONTEXT", None
)

ENABLE_TRANSLATIONS = ENABLE_REGISTRATIONS and "modeltranslation" in dj_settings.INSTALLED_APPS

# dj_settings example
# CAMOMILLA = {
#     "PROJECT_TITLE": "",
#     "ROUTER": {
#         "BASE_URL": ""
#     },
#     "MEDIA": {
#         "OPTIMIZE": {"WIDTH": 50, "HEIGHT": 50},
#         "THUMBNAIL": {"FOLDER": "", "WIDTH": 50, "HEIGHT": 50}
#     },
#     "RENDER": {
#         "ARTICLE": {"DEFAULT_TEMPLATE": "", "INJECT_CONTEXT": None },
#         "PAGE": {"DEFAULT_TEMPLATE": "", "INJECT_CONTEXT": None }
#     }
# }
