from django.conf import settings
from hvad.contrib.restframework import TranslationsMixin
from rest_framework import serializers
from django.utils import translation


class LangInfoMixin(metaclass=serializers.SerializerMetaclass):
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

    def get_default_field_names(self, *args):
        field_names = super().get_default_field_names(*args)
        self.action = getattr(
            self, "action", self.context and self.context.get("action", "list")
        )
        if self.action != "retrieve":
            return [f for f in field_names if f != "lang_info"]
        return field_names


class TranslationSetMixin(TranslationsMixin):
    def get_default_field_names(self, *args):
        field_names = super(TranslationsMixin, self).get_default_field_names(*args)
        self.action = getattr(
            self, "action", self.context and self.context.get("action", "list")
        )
        if self.action != "list":
            field_names += [self.Meta.model._meta.translations_accessor]
        return field_names


class SetupEagerLoadingMixin:
    @staticmethod
    def setup_eager_loading(queryset):
        return queryset
