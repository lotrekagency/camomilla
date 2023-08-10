import django
from django.conf import settings as django_settings
from django.db.models.aggregates import Max
from django.db.models.functions import Coalesce
from django.utils import translation
from modeltranslation.settings import AVAILABLE_LANGUAGES
from modeltranslation.utils import build_localized_fieldname
from rest_framework import serializers
from rest_framework.utils import model_meta

from camomilla.fields import ORDERING_ACCEPTED_FIELDS
from camomilla.serializers.fields.related import RelatedField
from camomilla.serializers.utils import build_standard_model_serializer
from camomilla.serializers.validators import UniquePermalinkValidator
from camomilla.utils import dict_merge
from camomilla import settings

if django.VERSION >= (4, 0):
    from django.db.models import JSONField as DjangoJSONField
else:
    from django.contrib.postgres.fields import JSONField as DjangoJSONField


# TODO: decide what to do with LangInfoMixin mixin!
class LangInfoMixin(metaclass=serializers.SerializerMetaclass):
    lang_info = serializers.SerializerMethodField("get_lang_info", read_only=True)

    def get_lang_info(self, obj, *args, **kwargs):
        languages = []
        for key, language in django_settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return {
            "default": django_settings.LANGUAGE_CODE,
            "active": translation.get_language(),
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
    def is_json_field(self, attr, value, info):
        return (
            attr in info.fields
            and isinstance(info.fields[attr], DjangoJSONField)
            and isinstance(value, dict)
        )

    def update(self, instance, validated_data):
        if self.partial:
            info = model_meta.get_field_info(instance)
            for attr, value in validated_data.items():
                if self.is_json_field(attr, value, info):
                    validated_data[attr] = dict_merge(
                        getattr(instance, attr, {}), value
                    )
        return super().update(instance, validated_data)


class NestMixin:
    def __init__(self, *args, **kwargs):
        self._depth = kwargs.pop("depth", None)
        return super().__init__(*args, **kwargs)

    def build_nested_field(self, field_name, relation_info, nested_depth):
        return self.build_relational_field(field_name, relation_info, nested_depth)

    def build_relational_field(
        self, field_name, relation_info, nested_depth=settings.API_NESTING_DEPTH + 1
    ):
        nested_depth = nested_depth if self._depth is None else self._depth
        field_class, field_kwargs = super().build_relational_field(
            field_name, relation_info
        )
        if (
            field_class is RelatedField and nested_depth > 1
        ):  # stop recursion one step before the jump :P
            field_kwargs["serializer"] = build_standard_model_serializer(
                relation_info[1], nested_depth - 1
            )
        return field_class, field_kwargs


class AbstractPageMixin(serializers.ModelSerializer):
    LANG_PERMALINK_FIELDS = [
        build_localized_fieldname("permalink", lang)
        for lang in AVAILABLE_LANGUAGES
        if settings.ENABLE_TRANSLATIONS
    ]

    @property
    def translation_fields(self):
        return super().translation_fields + ["permalink"]

    def get_default_field_names(self, *args):
        return (
            [f for f in super().get_default_field_names(*args) if f != "url_node"]
            + self.LANG_PERMALINK_FIELDS
            + ["permalink"]
        )

    def build_field(self, field_name, info, model_class, nested_depth):
        if field_name in self.LANG_PERMALINK_FIELDS + ["permalink"]:
            return serializers.CharField, {
                "source": "url_node.%s" % field_name,
                "read_only": True,
            }
        return super().build_field(field_name, info, model_class, nested_depth)

    def get_validators(self):
        return super().get_validators() + [UniquePermalinkValidator()]
