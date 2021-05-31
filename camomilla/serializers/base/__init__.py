from ..mixins import LangInfoMixin, SetupEagerLoadingMixin, TranslationSetMixin
from rest_framework import serializers
from hvad.contrib.restframework import TranslatableModelSerializer


class BaseModelSerializer(SetupEagerLoadingMixin, serializers.ModelSerializer):
    pass


class BaseTranslatableModelSerializer(
    LangInfoMixin, TranslationSetMixin, TranslatableModelSerializer
):
    pass
