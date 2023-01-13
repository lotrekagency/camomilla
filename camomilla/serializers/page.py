from ..models import Content, Page
from .base import BaseModelSerializer


class ContentSerializer(BaseModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(BaseModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
