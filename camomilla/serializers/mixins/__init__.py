from django.conf import settings
from hvad.contrib.restframework import TranslationsMixin
from rest_framework import serializers
from django.utils import translation
from django.db.models.aggregates import Max
from django.db.models.functions import Coalesce
from ...fields import ORDERING_ACCEPTED_FIELDS
from ...utils import dict_merge
from rest_framework.utils import model_meta
import django
from ..fields.related import RelatedField

if django.VERSION >= (4, 0):
    from django.db.models import JSONField as DjangoJSONField
else:
    from django.contrib.postgres.fields import JSONField as DjangoJSONField


class LangInfoMixin(metaclass=serializers.SerializerMetaclass):
    lang_info = serializers.SerializerMethodField("get_lang_info", read_only=True)

    def get_lang_info(self, obj, *args, **kwargs):
        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return {
            "default": settings.LANGUAGE_CODE,
            "active": translation.get_language(),
            "translated_in": obj.translations.all_languages(),
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


class OrderingMixin:
    def get_max_order(self, order_field):
        return self.Meta.model.objects.aggregate(
            max_order=Coalesce(Max(order_field), 0)
        )["max_order"]

    def _get_ordering_field_name(self):
        try:
            field_name = self.Meta.model._meta.ordering[0]
            if field_name[0] == "-":
                field_name = field_name[1:]
            return field_name
        except (AttributeError, IndexError):
            return None

    def build_standard_field(self, field_name, model_field):
        field_class, field_kwargs = super().build_standard_field(
            field_name, model_field
        )
        if (
            isinstance(model_field, ORDERING_ACCEPTED_FIELDS)
            and field_name == self._get_ordering_field_name()
        ):
            field_kwargs["default"] = self.get_max_order(field_name) + 1
        return field_class, field_kwargs


class JSONFieldPatchMixin:
    def update(self, instance, validated_data):
        if self.partial:
            info = model_meta.get_field_info(instance)
            for attr, value in validated_data.items():
                if (
                    attr in info.fields
                    and isinstance(info.fields[attr], DjangoJSONField)
                    and isinstance(value, dict)
                ):
                    validated_data[attr] = dict_merge(
                        getattr(instance, attr, {}), value
                    )
        return super().update(instance, validated_data)


DEFAULT_NESTING_DEPTH = 10


class NestMixin:
    def build_nested_field(self, field_name, relation_info, nested_depth):
        return self.build_relational_field(field_name, relation_info, nested_depth)

    def build_relational_field(
        self, field_name, relation_info, nested_depth=DEFAULT_NESTING_DEPTH + 1
    ):
        field_class, field_kwargs = super().build_relational_field(
            field_name, relation_info
        )
        if (
            field_class is RelatedField and nested_depth > 1
        ):  # stop recursion one step before the jump :P
            field_kwargs["serializer"] = self.build_standard_model_serializer(
                relation_info[1], nested_depth - 1
            )
        return field_class, field_kwargs
