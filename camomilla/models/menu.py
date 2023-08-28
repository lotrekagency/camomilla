from enum import Enum
from uuid import uuid4
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.safestring import mark_safe
from pydantic import (
    Field,
    SerializationInfo,
    computed_field,
    model_serializer,
)
from camomilla import structured
from camomilla.models.page import UrlNode
from typing import Optional, Union, Callable


class LinkTypes(str, Enum):
    relational = "RE"
    static = "ST"


class MenuNodeLink(structured.BaseModel):
    link_type: LinkTypes = LinkTypes.static
    static: str = None
    content_type: int = None
    page_id: int = None
    url_node: UrlNode = None

    @model_serializer(mode="wrap", when_used="json")
    def update_relational(self, handler: Callable, info: SerializationInfo):
        if self.link_type == LinkTypes.relational:
            if self.content_type and self.page_id:
                c_type = ContentType.objects.filter(pk=self.content_type).first()
                model = c_type and c_type.model_class()
                page = model and model.objects.filter(pk=self.page_id).first()
                self.url_node = page and page.url_node
        return handler(self)

    def get_url(self, request=None):
        if self.link_type == LinkTypes.relational:
            return isinstance(self.url_node, UrlNode) and self.url_node.routerlink
        elif self.link_type == LinkTypes.static:
            return self.static

    @computed_field
    @property
    def url(self) -> Optional[str]:
        return self.get_url()


class MenuNode(structured.BaseModel):
    id: str = Field(default_factory=uuid4)
    meta: dict = {}
    nodes: list["MenuNode"] = []
    title: str = ""
    link: MenuNodeLink


class Menu(models.Model):
    key = models.CharField(max_length=200, unique=True, editable=False)
    available_classes = models.JSONField(default=dict, editable=False)
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

    def __str__(self) -> str:
        return self.key
