from hvad.contrib.restframework.serializers import TranslationsMixin
from rest_framework import serializers

from ..models import Content, Page
from .media import MediaSerializer
from .mixins import CamomillaBaseTranslatableModelSerializer


class ContentSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(TranslationsMixin, CamomillaBaseTranslatableModelSerializer):
    og_image_exp = MediaSerializer(source="og_image", read_only=True)
    content_set = serializers.SerializerMethodField("get_translated_content")

    class Meta:
        model = Page
        fields = "__all__"

    def get_translated_content(self, obj):
        content = (
            Content.objects.language(self.ulanguage).fallbacks().filter(page__pk=obj.pk)
        )
        return ContentSerializer(content, many=True).data


class CompactPageSerializer(
    TranslationsMixin, CamomillaBaseTranslatableModelSerializer
):
    class Meta:
        model = Page
        fields = ("id", "identifier", "title", "description", "permalink", "og_image")
