from rest_framework import serializers

from camomilla.models import Media, MediaFolder
from camomilla.serializers.base import BaseModelSerializer
from camomilla.storages import OverwriteStorage


class MediaListSerializer(BaseModelSerializer):
    is_image = serializers.SerializerMethodField("get_is_image")

    def get_is_image(self, obj):
        return obj.is_image

    class Meta:
        model = Media
        fields = "__all__"


class MediaSerializer(BaseModelSerializer):
    links = serializers.SerializerMethodField("get_linked_instances")
    is_image = serializers.SerializerMethodField("get_is_image")

    class Meta:
        model = Media
        fields = "__all__"

    def get_linked_instances(self, obj):
        result = []
        links = obj.get_foreign_fields()
        for link in links:
            manager = getattr(obj, link)
            for item in manager.all():
                if item.__class__.__name__ != "MediaTranslation":
                    result.append(
                        {
                            "model": item.__class__.__name__,
                            "name": item.__str__(),
                            "id": item.pk,
                        }
                    )
        return result

    def update(self, instance, data):
        same_url = self.initial_data.get("same_url", False)
        if same_url:
            new_file = data.pop("file", None)
            if new_file:
                instance = super().update(instance, data)
                instance.file.storage = OverwriteStorage()
                instance.file.save(instance.file.name, new_file, save=True)
                return instance
        return super().update(instance, data)

    def get_is_image(self, obj):
        return obj.is_image


class MediaFolderSerializer(BaseModelSerializer):
    icon = MediaSerializer(read_only=True)

    class Meta:
        model = MediaFolder
        fields = "__all__"
