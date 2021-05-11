from rest_framework import serializers

from ..models import Media, MediaFolder
from .mixins import CamomillaBaseTranslatableModelSerializer


class MediaSerializer(CamomillaBaseTranslatableModelSerializer):
    links = serializers.SerializerMethodField("get_linked_instances")

    class Meta:
        model = Media
        fields = "__all__"

    def get_linked_instances(self, obj):
        result = []
        links = obj.get_foreign_fields()
        for link in links:
            manager = getattr(obj, link)
            if hasattr(manager, "language"):
                manager = manager.language()
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


class MediaFolderSerializer(CamomillaBaseTranslatableModelSerializer):
    icon = MediaSerializer(read_only=True)

    class Meta:
        model = MediaFolder
        fields = "__all__"
