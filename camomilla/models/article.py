from django.conf import settings
from django.db import models

from django.utils.translation import gettext_lazy as _

from hvad.models import TranslatedFields

from .mixins import SeoMixin, MetaMixin


CONTENT_STATUS = (
    ("PUB", _("Published")),
    ("DRF", _("Draft")),
    ("TRS", _("Trash")),
    ("PLA", _("Planned")),
)


class BaseArticle(SeoMixin, MetaMixin):

    seo_attr = "permalink"

    identifier = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields(
        content=models.TextField(default=""),
        permalink=models.SlugField(max_length=200, blank=False),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL
    )
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default="DRF",
    )
    highlight_image = models.ForeignKey(
        "camomilla.Media", blank=True, null=True, on_delete=models.SET_NULL
    )
    date = models.DateTimeField(auto_now=True)
    pubblication_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField("camomilla.Tag", blank=True)
    categories = models.ManyToManyField("camomilla.Category", blank=True)
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        unique_together = [("permalink", "language_code")]
        ordering = ["ordering"]

    def save(self, *args, **kwargs):
        import uuid

        if not self.identifier:
            self.identifier = "{0}".format(str(uuid.uuid4()))
        super(BaseArticle, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(BaseArticle):
    translations = TranslatedFields()
