from typing import Iterable, Tuple
from uuid import uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db import ProgrammingError, models, transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.http import Http404
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from camomilla.models.mixins import MetaMixin, SeoMixin
from camomilla.utils import (
    get_field_translations,
    get_nofallbacks,
    set_nofallbacks,
    url_lang_decompose,
    lang_fallback_query,
    activate_languages,
)

from modeltranslation.settings import ENABLE_REGISTRATIONS


class UrlNodeManager(models.Manager):
    @property
    def related_names(self):
        self._related_names = getattr(
            self,
            "_related_names",
            super().get_queryset().values_list("related_name", flat=True).distinct(),
        )
        return self._related_names

    def _annotate_fields(
        self,
        qs: models.QuerySet,
        field_names: Iterable[Tuple[str, models.Field, models.Value]],
    ):
        for field_name, output_field, default in field_names:
            whens = [
                models.When(
                    related_name=related_name,
                    then=models.F("__".join([related_name, field_name])),
                )
                for related_name in self.related_names
            ]
            qs = qs.annotate(
                **{
                    field_name: models.Case(
                        *whens, output_field=output_field, default=default
                    )
                }
            )
        return qs

    def get_queryset(self):
        try:
            return self._annotate_fields(
                super().get_queryset(),
                [
                    ("indexable", models.BooleanField(), models.Value(None, models.BooleanField())),
                    ("status", models.BooleanField(), models.Value(None, models.BooleanField())),
                    ("pubblication_date", models.DateTimeField(), models.Value(timezone.now(), models.DateTimeField())),
                ],
            )
        except ProgrammingError:
            return super().get_queryset()


class UrlNode(models.Model):
    permalink = models.CharField(max_length=400, unique=True, null=True)
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
    slug = models.SlugField(max_length=150, allow_unicode=True, null=True, blank=True)
    status = models.CharField(
        max_length=3,
        choices=PAGE_STATUS,
        default="DRF",
    )
    template = models.CharField(max_length=500, null=True, blank=True)
    identifier = models.CharField(max_length=200, null=True, unique=True)
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
        return "(%s) %s" % (self.__class__.__name__, self.title or self.permalink)

    def get_context(self, request=None):
        return {
            "page": self,
            "page_model": {"class": self.__class__.__name__, "module": self.__module__},
            "request": request,
        }

    @property
    def model_name(self):
        return self._meta.app_label + "." + self._meta.model_name

    @property
    def model_info(self):
        return {"app_label": self._meta.app_label, "class": self._meta.model_name}

    @property
    def permalink(self):
        return self.url_node and self.url_node.permalink

    @property
    def breadcrumbs(self):
        breadcrumb = {
            "permalink": self.permalink,
            "title": self.breadcrumbs_title or self.title or self.slug,
        }
        if self.parent:
            return self.parent.breadcrumbs + [breadcrumb]
        return [breadcrumb]

    @property
    def is_public(self):
        if self.status == "PUB":
            return True
        if self.status == "PLA":
            return bool(self.pubblication_date) and timezone.now() > self.pubblication_date
        return False

    @property
    def template_name(self):
        return self.template or "defaults/pages/default.html"

    @property
    def childs(self):
        if hasattr(self, "PageMeta") and hasattr(self.PageMeta, "child_page_field"):
            return getattr(self, self.PageMeta.child_page_field)
        return getattr(self, PAGE_CHILD_RELATED_NAME % self.model_info)

    @property
    def parent(self):
        if hasattr(self, "PageMeta") and hasattr(self.PageMeta, "parent_page_field"):
            return getattr(self, self.PageMeta.parent_page_field)
        return self.parent_page

    def _get_or_create_url_node(self) -> UrlNode:
        if not self.url_node:
            self.url_node = UrlNode.objects.create(
                related_name=URL_NODE_RELATED_NAME % self.model_info
            )
        return self.url_node

    def _update_url_node(self, force=False):
        self.url_node = self._get_or_create_url_node()
        for _ in activate_languages():
            old_permalink = self.permalink
            new_permalink = self.generate_permalink()
            force = force or old_permalink != new_permalink
            set_nofallbacks(self.url_node, "permalink", new_permalink)
        if force:
            self.url_node.save()
            self.update_childs()
        return self.url_node

    def generate_permalink(self):
        slug = get_nofallbacks(self, "slug")
        if slug is None:
            translations = get_field_translations(self, "slug").values()
            fallback_slug = next((t for t in translations if t is not None), None)
            slug = (
                slugify(self.title or uuid4(), allow_unicode=True)
                if fallback_slug is None
                else fallback_slug
            )
            set_nofallbacks(self, "slug", slug)
        permalink = "/%s" % slugify(slug, allow_unicode=True)
        if self.parent:
            permalink = f"{self.parent.permalink}{permalink}"
        qs = UrlNode.objects.exclude(pk=getattr(self.url_node or object, "pk", None))
        if qs.filter(permalink=permalink).exists():
            permalink = "/".join(
                permalink.split("/")[:-1] + [slugify(uuid4(), allow_unicode=True)]
            )
        return permalink

    def update_childs(self):
        # without pk, no childs there
        if self.pk is not None:
            for child in self.childs.all():
                child.save()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self._update_url_node()
            return super().save(*args, **kwargs)

    @classmethod
    def get(cls, request, *args, **kwargs):
        bypass_type_check = kwargs.pop("bypass_type_check", False)
        bypass_public_check = kwargs.pop("bypass_public_check", False)

        if len(kwargs.keys()) > 0:
            page = cls.objects.get(**kwargs)
        else:
            node = UrlNode.objects.filter(
                permalink=url_lang_decompose(request.path)["permalink"]
            ).first()
            page = node and node.page
        type_error = not bypass_type_check and not isinstance(page, cls)
        public_error = not bypass_public_check and not getattr(page or object, "is_public", False)
        if not page or type_error or public_error:
            bases = (UrlNode.DoesNotExist,)
            if hasattr(cls, "DoesNotExist"):
                bases += (cls.DoesNotExist,)
            raise type("PageDoesNotExist", bases, {})(
                "%s matching query does not exist." % cls._meta.object_name
            )
        return page

    @classmethod
    def get_or_create(cls, request, *args, **kwargs):
        try:
            return cls.get(request, *args, **kwargs), False
        except ObjectDoesNotExist:
            if len(kwargs.keys()) > 0:
                return cls.objects.get_or_create(**kwargs)
        return (None, False)

    @classmethod
    def get_or_create_homepage(cls):
        try:
            if ENABLE_REGISTRATIONS:
                node = UrlNode.objects.get(lang_fallback_query(permalink="/"))
            else:
                node = UrlNode.objects.get(permalink="/")
            return node.page, False
        except UrlNode.DoesNotExist:
            return cls.get_or_create(None, slug="")

    @classmethod
    def get_or_404(cls, request, *args, **kwargs):
        try:
            return cls.get(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404("No %s matches the given query." % cls._meta.object_name)

    def alternate_urls(self, *args, **kwargs):
        return get_field_translations(self.url_node or object, "permalink", None)

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
        instance.url_node and instance.url_node.delete()
