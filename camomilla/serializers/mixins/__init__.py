from django.conf import settings
from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework import serializers
from django.utils import translation


class LangInfoMixin:
    lang_info = serializers.SerializerMethodField("get_lang_info", read_only=True)

    def get_lang_info(self, obj, *args, **kwargs):
        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return {
            "default": settings.LANGUAGE_CODE,
            "active": translation.get_language(),
            "translated_in": obj.get_available_languages(),
            "site_languages": languages,
        }


class CamomillaBaseTranslatableModelSerializer(
    LangInfoMixin, TranslatableModelSerializer
):
    pass
