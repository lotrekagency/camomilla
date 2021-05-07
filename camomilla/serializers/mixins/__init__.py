from django.conf import settings
from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework import serializers


class CamomillaBaseTranslatableModelSerializer(TranslatableModelSerializer):
    translated_languages = serializers.SerializerMethodField(
        "get_available_translations", read_only=True
    )
    active_languages = serializers.SerializerMethodField(
        "get_active_languages", read_only=True
    )

    def get_available_translations(self, obj):
        return obj.get_available_languages()

    def get_active_languages(self, request, *args, **kwargs):
        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return {"active": settings.LANGUAGE_CODE, "languages": languages}
