from typing import Iterable
from django.apps import apps
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .mixins import MetaMixin, SeoMixin


class UrlNodeManager(models.Manager):
    @property
    def related_names(self):
        self._related_names = getattr(
            self,
            "_related_names",
            self.values_list("related_name", flat=True).distinct(),
        )
        return self._related_names

    def _annotate_fields(self, qs: models.QuerySet, field_names: Iterable[str]):
        for field_name in field_names:
            whens = []
            for related_name in self.related_names:
                whens.append(
                    models.When(
                        related_name=related_name,
                        then=models.F("__".join([related_name, field_name])),
                    )
                )
            qs = qs.annotate(**{field_name: models.Case(*whens)})
        return qs

    # def get_queryset(self):
    #     return self._annotate_fields(super().get_queryset(), ["indexable", "status"])


class UrlNode(models.Model):
    permalink = models.CharField(max_length=400, unique=True)
    related_name = models.CharField(max_length=200)
    objects = UrlNodeManager()

    @property
    def page(self):
        return getattr(self, self.related_name)


PAGE_CHILD_RELATED_NAME = "%(app_label)s_%(class)s_child_pages"
URL_NODE_RELATED_NAME = "%(app_label)s_%(class)s"

PAGE_STATUS = (
    ("PUB", _("Published")),
    ("DRF", _("Draft")),
    ("TRS", _("Trash")),
    ("PLA", _("Planned")),
)


class AbstractPage(SeoMixin, MetaMixin, models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated_at = models.DateTimeField(auto_now=True)
    url_node = models.OneToOneField(
        UrlNode, on_delete=models.CASCADE, related_name=URL_NODE_RELATED_NAME, null=True
    )
    breadcrumbs_title = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=150, allow_unicode=True, blank=True)
    status = models.CharField(
        max_length=3,
        choices=PAGE_STATUS,
        default="DRF",
    )
    pubblication_date = models.DateTimeField(null=True, blank=True)
    indexable = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)
    parent_page = models.ForeignKey(
        "self",
        related_name=PAGE_CHILD_RELATED_NAME,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "(%s) %s at %s" % (self.__class__.__name__, self.title, self.permalink)

    @property
    def model_name(self):
        return self._meta.app_label + "." + self._meta.model_name

    @property
    def model_info(self):
        return {"app_label": self._meta.app_label, "class": self._meta.model_name}

    @property
    def permalink(self):
        return self.safe_url_node.permalink

    @property
    def safe_url_node(self):
        if not self.url_node:
            self.url_node = UrlNode.objects.create(
                permalink=self.generate_permalink(),
                related_name=URL_NODE_RELATED_NAME % self.model_info,
            )
            super().save(update_fields=["url_node"])
        return self.url_node

    @property
    def breadcrumbs(self):
        breadcrumb = {
            "permalink": self.permalink,
            "title": self.breadcrumbs_title or self.title or self.slug,
        }
        if self.parent_page:
            return self.parent_page.breadcrumbs + [breadcrumb]
        return [breadcrumb]

    def update_url_node(self, permalink, force=False):
        changed = self.safe_url_node.permalink != permalink
        if changed or force:
            self.safe_url_node.permalink = permalink
            self.safe_url_node.save(update_fields=["permalink"])
        if changed:
            self.update_childs()
        return self.safe_url_node

    def generate_permalink(self):
        permalink = slugify(self.slug or "", allow_unicode=True)
        if self.parent_page:
            permalink = f"{self.parent_page.permalink}/{permalink}"
        return permalink

    def update_childs(self):
        for child in getattr(self, PAGE_CHILD_RELATED_NAME % self.model_info).all():
            child.save()

    def save(self, *args, **kwargs):
        old_permalink = self.permalink
        new_permalink = self.generate_permalink()
        if old_permalink != new_permalink:
            self.update_url_node(new_permalink)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ("ordering",)
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")


class Page(AbstractPage):
    pass


@receiver(post_delete)
def auto_delete_url_node(sender, instance, **kwargs):
    if issubclass(sender, AbstractPage):
        instance.url_node.delete()
