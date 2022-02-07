from ..models import Content, Page
from .fields import RelatedField
from .media import MediaSerializer
from .base import BaseTranslatableModelSerializer


class ContentSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(BaseTranslatableModelSerializer):
    og_image = RelatedField(serializer=MediaSerializer, required=False, allow_null=True)
    contents = RelatedField(
        serializer=ContentSerializer, many=True, required=False, allow_null=True
    )

    class Meta:
        model = Page
        fields = "__all__"
