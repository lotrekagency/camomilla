from django.db import models
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    key = models.CharField(max_length=200, unique=True)
    available_classes = models.JSONField(default=dict)
    enabled = models.BooleanField(default=True)
    nodes = models.JSONField(default=list)

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")
