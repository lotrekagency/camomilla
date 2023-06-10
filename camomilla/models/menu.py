from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class Menu(models.Model):
    # TODO: rewtrite menu nodes with StructuredJSONField:
    key = models.CharField(max_length=200, unique=True)
    available_classes = models.JSONField(default=dict)
    enabled = models.BooleanField(default=True)
    nodes = models.JSONField(default=list)

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def render(self, request=None):
        return mark_safe(
            render_to_string("defaults/parts/menu.html", {"menu": self}, request)
        )

    class defaultdict(dict):
        def __missing__(self, key):
            dict.__setitem__(self, key, Menu.objects.get_or_create(key=key)[0])
            return self[key]
