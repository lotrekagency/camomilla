import os
from django.conf import settings


settings.configure(
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3"}},
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
        }
    ],
    AES_ENCRIPTION_KEY="abcdefgh01234567",
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "camomilla",
        "rest_framework.authtoken",
    ],
    ROOT_URLCONF="tests.urls",
    LANGUAGE_CODE="it",
    LANGUAGES=(
        ("it", "Italian"),
        ("en", "English"),
        ("de", "German"),
    ),
    USE_I18N=True,
    USE_L10N=True,
    THUMB_FOLDER="thumbnails",
    REST_FRAMEWORK={
        "DEFAULT_PARSER_CLASSES": (
            "rest_framework.parsers.JSONParser",
            "rest_framework.parsers.FormParser",
            "rest_framework.parsers.MultiPartParser",
        ),
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ),
    },
)
