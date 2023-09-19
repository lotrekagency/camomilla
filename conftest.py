import os
from django.conf import settings
import shutil
from django.core.management import call_command
from django.db import connections
import pytest
from devtools import debug


def clean_migration_folders():
    from django.conf import settings

    for dir in settings.MIGRATION_MODULES.values():
        debug("Removing", dir, os.path.exists(dir))
        if os.path.exists(dir):
            shutil.rmtree(dir)


def create_migration_folders():
    from django.conf import settings

    for dir in settings.MIGRATION_MODULES.values():
        debug("Creating", dir, os.path.exists(dir))
        if not os.path.exists(dir):
            os.makedirs(dir)
            open(os.path.join(dir, "__init__.py"), "w").close()


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker):
    from django.conf import settings

    create_migration_folders()
    test_db = "test_db"
    settings.DATABASES["default"]["NAME"] = test_db

    with django_db_blocker.unblock():
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)

    yield
    for connection in connections.all():
        connection.close()
    # clean_migration_folders()


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
        "rest_framework",
        "rest_framework.authtoken",
        "camomilla.theme",
        "modeltranslation",
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
