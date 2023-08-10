from camomilla.serializers.mixins import AbstractPageMixin
from camomilla.models import Content, Page
from camomilla.serializers.base import BaseModelSerializer


class ContentSerializer(BaseModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class PageSerializer(AbstractPageMixin, BaseModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
