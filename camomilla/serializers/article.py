from camomilla.models import Article, Tag
from camomilla.serializers.base import BaseModelSerializer
from camomilla.serializers.mixins import AbstractPageMixin


class TagSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(AbstractPageMixin, BaseModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
