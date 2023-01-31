from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .page import AbstractPage


class AbstractArticle(AbstractPage):

    content = models.TextField(default="")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL
    )
    highlight_image = models.ForeignKey(
        "camomilla.Media",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_highlight_images",
    )
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        abstract = True
        ordering = ["ordering"]


class Article(AbstractArticle):
    pass


class AbstractTag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "(%s) %s" % (self.__class__.__name__, self.name)

class Tag(AbstractTag):
    pass
