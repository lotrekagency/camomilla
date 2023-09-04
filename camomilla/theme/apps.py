from __future__ import unicode_literals
from collections import OrderedDict

from django.apps import AppConfig, apps
from django.conf import settings


class CamomillaThemeConfig(AppConfig):
    name = "camomilla.theme"

    def ready(self):
        installed_apps = getattr(settings, "INSTALLED_APPS", [])
        changed = False
        if "django_jsonform" not in installed_apps:
            changed = True
            installed_apps = ["django_jsonform", *installed_apps]
        if "admin_interface" not in installed_apps:
            changed = True
            installed_apps = ["admin_interface", *installed_apps]
        if "colorfield" not in installed_apps:
            changed = True
            installed_apps = ["colorfield", *installed_apps]
        if changed:
            setattr(settings, "INSTALLED_APPS", installed_apps)
            apps.app_configs = OrderedDict()
            apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False
            apps.clear_cache()
            apps.populate(settings.INSTALLED_APPS)
        setattr(
            settings,
            "X_FRAME_OPTIONS",
            getattr(
                settings,
                "X_FRAME_OPTIONS",
                "SAMEORIGIN"
            ),
        )
