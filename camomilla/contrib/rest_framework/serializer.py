from functools import cached_property
from typing import Iterable, Union
from django.http import QueryDict

from modeltranslation import settings as mt_settings
from modeltranslation.translator import NotRegistered, translator
from modeltranslation.utils import build_localized_fieldname
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from camomilla.utils.getters import pointed_getter
from camomilla.utils.translation import is_translatable


TRANS_ACCESSOR = "translations"


def plain_to_nest(data, fields, accessor=TRANS_ACCESSOR):
    """
    This function transforms a plain dictionary with translations fields (es. {"title_en": "Hello"})
    into a dictionary with nested translations fields (es. {"translations": {"en": {"title": "Hello"}}}).
    """
    trans_data = {}
    for lang in mt_settings.AVAILABLE_LANGUAGES:
        lang_data = {}
        for field in fields:
            trans_field_name = build_localized_fieldname(field, lang)
            if trans_field_name in data:
                lang_data[field] = data.pop(trans_field_name)
        if lang_data.keys():
            trans_data[lang] = lang_data
    if trans_data.keys():
        data[accessor] = trans_data
    return data


def nest_to_plain(data: Union[dict, QueryDict], fields: list[str], accessor=TRANS_ACCESSOR):
    """
    This function is the inverse of plain_to_nest.
    It transforms a dictionary with nested translations fields (es. {"translations": {"en": {"title": "Hello"}}})
    into a plain dictionary with translations fields (es. {"title_en": "Hello"}).
    """
    if isinstance(data, QueryDict):
        data = data.dict()
    translations = data.pop(accessor, {})
    for lang in mt_settings.AVAILABLE_LANGUAGES:
        nest_trans = translations.pop(lang, {})
        for k in fields:
            data.pop(k, None)  # this removes all trans field without lang
            if k in nest_trans:
                # this saves on the default field the default language value
                if lang == mt_settings.DEFAULT_LANGUAGE:
                    data[k] = nest_trans[k]
                key = build_localized_fieldname(k, lang)
                data[key] = data.get(key, nest_trans[k])
    return data


class TranslationsMixin(serializers.ModelSerializer):
    """
    This mixin adds support for modeltranslation fields.
    It automatically nests all translations fields (es. title_en) under a "translations" field.

    This means that, in representation, the serializer will transform:
    `{"title_en": "Hello", "title_it": "Ciao"}` -> `{"translations": {"en": {"title": "Hello"}, "it": {"title": "Ciao"}}`

    While in deserialization, the serializer will transform:
    `{"translations": {"en": {"title": "Hello"}, "it": {"title": "Ciao"}}` -> `{"title_en": "Hello", "title_it": "Ciao"}`
    """

    @cached_property
    def translation_fields(self) -> list[str]:
        try:
            return translator.get_options_for_model(self.Meta.model).get_field_names()
        except NotRegistered:
            return []

    @property
    def _writable_fields(self) -> Iterable[serializers.Field]:
        for field in super()._writable_fields:
            if field.field_name not in self.translation_fields:
                yield field

    def to_internal_value(self, data):
        if self.translation_fields:
            nest_to_plain(data, self.translation_fields)
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.translation_fields:
            plain_to_nest(representation, self.translation_fields)
        return representation

    def run_validation(self, *args, **kwargs):
        try:
            return super().run_validation(*args, **kwargs)
        except ValidationError as ex:
            if self.translation_fields:
                plain_to_nest(ex.detail, self.translation_fields)
            raise ValidationError(detail=ex.detail)

    @property
    def is_translatable(self):
        return is_translatable(pointed_getter(self, "Meta.model"))


class RemoveTranslationsMixin(serializers.ModelSerializer):
    """
    This mixin removes all translations fields (es. title_en) from the serializer.
    It's useful when you want to create a serializer that doesn't need to include all translations fields.

    If request is passed in context, this serializer becomes aware of the query parameter "included_translations".
    If the value is "all", all translations fields are included.
    If the value is a comma separated list of languages (es. "en,it"), only the specified translations fields are included.
    """

    @cached_property
    def translation_fields(self):
        try:
            return translator.get_options_for_model(self.Meta.model).get_field_names()
        except NotRegistered:
            return []

    def get_default_field_names(self, declared_fields, model_info):
        request = self.context.get("request", False)
        included_translations = request and request.GET.get(
            "included_translations", False
        )
        if included_translations == "all":
            return super().get_default_field_names(declared_fields, model_info)
        elif included_translations is not False:
            included_translations = included_translations.split(",")
        else:
            included_translations = []

        field_names = super().get_default_field_names(declared_fields, model_info)
        for lang in mt_settings.AVAILABLE_LANGUAGES:
            if lang not in included_translations:
                for field in self.translation_fields:
                    localized_fieldname = build_localized_fieldname(field, lang)
                    if localized_fieldname in field_names:
                        field_names.remove(localized_fieldname)
        return field_names
