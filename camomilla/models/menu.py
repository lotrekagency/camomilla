from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.safestring import mark_safe
from camomilla import structured
from camomilla.models.page import UrlNode
from typing import Union


class MenuNodeLink(structured.Model):
    link_type = structured.CharField()
    static = structured.CharField()
    url_node = structured.ForeignKey(UrlNode)
    content_type = structured.IntegerField()
    page_id = structured.IntegerField()

    @classmethod
    def to_db_transform(cls, data):
        if data.get("link_type", None) == "RE":
            ct_id = data.get("content_type", None)
            p_id = data.get("page_id", None)
            if ct_id and p_id:
                c_type = ContentType.objects.filter(pk=ct_id).first()
                model = c_type and c_type.model_class()
                page = model and model.objects.filter(pk=p_id).first()
                if page:
                    data["url_node"] = page.url_node.pk
                else:
                    data["url_node"] = None
        return data

    def get_url(self, request=None):
        if self.link_type == "RE":
            return self.url_node and self.url_node.routerlink
        elif self.link_type == "ST":
            return self.static

    @property
    def url(self):
        return self.get_url()


class MenuNode(structured.Model):
    id = structured.CharField()
    meta = structured.DictField()
    nodes = structured.ListField(items_types=("MenuNode",))
    title = structured.CharField()
    link = structured.EmbeddedField("MenuNodeLink")

    @classmethod
    def to_db_transform(cls, data):
        link = data.pop("link", {})
        nodes = data.pop("nodes", {})
        return {
            "link": MenuNodeLink.to_db_transform(link),
            "nodes": [cls.to_db_transform(n) for n in nodes],
            **data,
        }


class Menu(models.Model):
    key = models.CharField(max_length=200, unique=True)
    available_classes = models.JSONField(default=dict)
    enabled = models.BooleanField(default=True)
    nodes = structured.StructuredJSONField(default=list, schema=MenuNode)

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def render(
        self,
        template_path: str,
        request=None,
        context: Union[dict, RequestContext] = {},
    ):
        if isinstance(context, RequestContext):
            context = context.flatten()
        context.update({"menu": self})
        return mark_safe(render_to_string(template_path, context, request))

    class defaultdict(dict):
        def __missing__(self, key):
            dict.__setitem__(self, key, Menu.objects.get_or_create(key=key)[0])
            return self[key]
