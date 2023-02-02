from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):
    verbose_name = serializers.SerializerMethodField()
    verbose_name_plural = serializers.SerializerMethodField()

    def get_verbose_name(self, obj):
        return obj.model_class()._meta.verbose_name.title()

    def get_verbose_name_plural(self, obj):
        return obj.model_class()._meta.verbose_name_plural.title()

    class Meta:
        model = ContentType
        fields = "__all__"
