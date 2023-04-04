from ..models import Content, Page
from .base import BaseTranslatableModelSerializer


class ContentSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
