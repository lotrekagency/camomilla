from django.conf import settings


PROJECT_TITLE = getattr(settings, "CAMOMILLA_PROJECT_TITLE", "Camomilla")

THUMBNAIL_FOLDER = getattr(settings, "CAMOMILLA_THUMBTHUMBNAIL_FOLDER", "thumbnails")
THUMBNAIL_WIDTH = getattr(settings, "CAMOMILLA_THUMBNAIL_WIDTH", 50)
THUMBNAIL_HEIGHT = getattr(settings, "CAMOMILLA_THUMBNAIL_HEIGHT", 50)
MEDIA_MAX_WIDTH = getattr(settings, "CAMOMILLA_MAX_WIDTH", 1920)
MEDIA_MAX_HEIGHT = getattr(settings, "CAMOMILLA_MAX_HEIGHT", 1080)
MEDIA_DPI = getattr(settings, "CAMOMILLA_MEDIA_DPI", 72)
MEDIA_BREAKPOINTS = getattr(settings, "CAMOMILLA_MEDIA_BREAKPOINTS", {"sm": 480, "md": 768, "lg": 1280})