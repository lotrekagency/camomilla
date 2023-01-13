from functools import cached_property
from rest_framework import serializers
from modeltranslation.translator import translator, NotRegistered
from modeltranslation import settings as mt_settings
from rest_framework.exceptions import ValidationError
from django.utils.translation import get_language

TRANS_ACCESSOR = "translations"


def plain_to_nest(data, options, accessor=TRANS_ACCESSOR):
    trans_data = {}
    for lang in mt_settings.AVAILABLE_LANGUAGES:
        lang_data = {}
        for base_field, fields in options.fields.items():
            trans_field = next(
                (f for f in fields if f.name.endswith("_%s" % lang)),
                object,
            )
            if trans_field.name in data:
                lang_data[base_field] = data.pop(trans_field.name)
        if lang_data.keys():
            trans_data[lang] = lang_data
    if trans_data.keys():
        data[accessor] = trans_data
    return data


def nest_to_plain(data, options, accessor=TRANS_ACCESSOR):
    translations = data.pop(accessor, {})
    for lang in mt_settings.AVAILABLE_LANGUAGES:
        nest_trans = translations.pop(lang, {})
        for k in options.fields.keys():
            data.pop(k, None) # this removes all trans field without lang
            if k in nest_trans:
                data["%s_%s" % (k, lang)] = nest_trans[k]
    return data


class TranslationsMixin(serializers.ModelSerializer):
    @cached_property
    def translations_options(self):
        try:
            return translator.get_options_for_model(self.Meta.model)
        except NotRegistered:
            return None

    def to_internal_value(self, data):
        if self.translations_options:
            nest_to_plain(data, self.translations_options)
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.translations_options:
            plain_to_nest(representation, self.translations_options)
        return representation

    def run_validation(self, *args, **kwargs):
        try:
            return super().run_validation(*args, **kwargs)
        except ValidationError as ex:
            if self.translations_options:
                plain_to_nest(ex.detail, self.translations_options)
            raise ValidationError(detail=ex.detail)
