from ..utils import get_camomilla_model
from .base import BaseTranslatableModelSerializer


class ContentSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = get_camomilla_model("content")
        fields = "__all__"


class PageSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = get_camomilla_model("page")
        fields = "__all__"
