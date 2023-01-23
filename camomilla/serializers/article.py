from .base import BaseTranslatableModelSerializer
from ..utils import get_camomilla_model


class TagSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = get_camomilla_model("tag")
        fields = "__all__"


class CategorySerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = get_camomilla_model("category")
        fields = "__all__"


class ArticleSerializer(BaseTranslatableModelSerializer):
    class Meta:
        model = get_camomilla_model("article")
        fields = "__all__"
