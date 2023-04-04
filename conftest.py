import os
from django.conf import settings

from django.core.management import call_command
from django.db import connections
import pytest

# # UNCOMMENT THIS TO TEST WITH A LOCAL SQLITE DB FIXTURE

# @pytest.fixture(scope='session')
# def django_db_setup(django_db_blocker):
#     from django.conf import settings
#     test_db = 'test_db'
#     settings.DATABASES['default']['NAME'] = test_db

#     with django_db_blocker.unblock():
#         call_command('migrate', '--noinput')
#     yield
#     for connection in connections.all():
#         connection.close()


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
