from ..models import Content, Page
from .fields import RelatedField
from .media import MediaSerializer
from .mixins import CamomillaBaseTranslatableModelSerializer


class ContentSerializer(CamomillaBaseTranslatableModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(CamomillaBaseTranslatableModelSerializer):
    og_image = RelatedField(serializer=MediaSerializer, allow_null=True)
    contents = RelatedField(serializer=ContentSerializer, many=True, allow_null=True)

    class Meta:
        model = Page
        fields = "__all__"
