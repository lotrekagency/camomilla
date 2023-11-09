from typing import Sequence, Tuple
from uuid import uuid4

from django.core.exceptions import ObjectDoesNotExist
from django.db import ProgrammingError, OperationalError, models, transaction
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.http import Http404
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.functional import lazy
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from camomilla.models.mixins import MetaMixin, SeoMixin
from camomilla.utils import (
    activate_languages,
    get_field_translations,
    get_nofallbacks,
    lang_fallback_query,
    set_nofallbacks,
    url_lang_decompose,
    get_all_templates_files,
)
from camomilla.utils.getters import pointed_getter
from camomilla import settings
from camomilla.templates_context.rendering import ctx_registry
from django.conf import settings as django_settings


def GET_TEMPLATE_CHOICES():
    return [(t, t) for t in get_all_templates_files()]


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
        field_names: Sequence[Tuple[str, models.Field, models.Value]],
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
        return self._annotate_is_public(qs)

    def _annotate_is_public(self, qs: models.QuerySet):
        return qs.annotate(
            is_public=models.Case(
                models.When(status="PUB", then=True),
                models.When(
                    status="PLA", publication_date__lte=timezone.now(), then=True
                ),
                default=False,
                output_field=models.BooleanField(default=False),
            )
        )

    def get_queryset(self):
        try:
            return self._annotate_fields(
                super().get_queryset(),
                [
                    (
                        "indexable",
                        models.BooleanField(),
                        models.Value(None, models.BooleanField()),
                    ),
                    (
                        "status",
                        models.CharField(),
                        models.Value("DRF", models.CharField()),
                    ),
                    (
                        "publication_date",
                        models.DateTimeField(),
                        models.Value(timezone.now(), models.DateTimeField()),
                    ),
                    (
                        "date_updated_at",
                        models.DateTimeField(),
                        models.Value(timezone.now(), models.DateTimeField()),
                    ),
                ],
            )
        except (ProgrammingError, OperationalError):
            return super().get_queryset()


class UrlNode(models.Model):
    permalink = models.CharField(max_length=400, unique=True, null=True)
    related_name = models.CharField(max_length=200)
    objects = UrlNodeManager()

    @property
    def page(self) -> "AbstractPage":
        return getattr(self, self.related_name)

    @staticmethod
    def reverse_url(permalink: str) -> str:
        append_slash = getattr(django_settings, "APPEND_SLASH", True)
        try:
            if permalink == "/":
                return reverse("camomilla-homepage")
            url = reverse("camomilla-permalink", args=(permalink.lstrip("/"),))
            if append_slash and not url.endswith("/"):
                url += "/"
            return url
        except NoReverseMatch:
            return None

    @property
    def routerlink(self) -> str:
        return self.reverse_url(self.permalink) or self.permalink

    def get_absolute_url(self) -> str:
        if self.routerlink == "/":
            return ""
        return self.routerlink


PAGE_CHILD_RELATED_NAME = "%(app_label)s_%(class)s_child_pages"
URL_NODE_RELATED_NAME = "%(app_label)s_%(class)s"

PAGE_STATUS = (
    ("PUB", _("Published")),
    ("DRF", _("Draft")),
    ("TRS", _("Trash")),
    ("PLA", _("Planned")),
)


class PageBase(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        attr_meta = attrs.pop("PageMeta", None)
        new_class = super().__new__(cls, name, bases, attrs, **kwargs)
        page_meta = attr_meta or getattr(new_class, "PageMeta", None)
        base_page_meta = getattr(new_class, "_page_meta", None)
        if page_meta:
            for name, value in getattr(base_page_meta, "__dict__", {}).items():
                if name not in page_meta.__dict__:
                    setattr(page_meta, name, value)
            setattr(new_class, "_page_meta", page_meta)
        return new_class


class AbstractPage(SeoMixin, MetaMixin, models.Model, metaclass=PageBase):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated_at = models.DateTimeField(auto_now=True)
    url_node = models.OneToOneField(
        UrlNode,
        on_delete=models.CASCADE,
        related_name=URL_NODE_RELATED_NAME,
        null=True,
        editable=False,
    )
    breadcrumbs_title = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=150, allow_unicode=True, null=True, blank=True)
    status = models.CharField(
        max_length=3,
        choices=PAGE_STATUS,
        default="DRF",
    )
    template = models.CharField(max_length=500, null=True, blank=True, choices=[])
    template_data = models.JSONField(default=dict, null=False, blank=True)
    identifier = models.CharField(max_length=200, null=True, unique=True, default=uuid4)
    publication_date = models.DateTimeField(null=True, blank=True)
    indexable = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)
    parent_page = models.ForeignKey(
        "self",
        related_name=PAGE_CHILD_RELATED_NAME,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __init__(self, *args, **kwargs):
        super(AbstractPage, self).__init__(*args, **kwargs)
        self._meta.get_field("template").choices = lazy(GET_TEMPLATE_CHOICES, list)()

    def __str__(self) -> str:
        return "(%s) %s" % (self.__class__.__name__, self.title or self.permalink)

    def get_context(self, request=None):
        context = {
            "page": self,
            "page_model": {"class": self.__class__.__name__, "module": self.__module__},
            "request": request,
        }
        inject_func = pointed_getter(self, "_page_meta.inject_context_func")
        if inject_func and callable(inject_func):
            new_ctx = inject_func(request=request, super_ctx=context)
            if isinstance(new_ctx, dict):
                context.update(new_ctx)
        return ctx_registry.get_context_for_page(self, request, super_ctx=context)

    @property
    def model_name(self) -> str:
        return self._meta.app_label + "." + self._meta.model_name

    @property
    def model_info(self) -> dict:
        return {"app_label": self._meta.app_label, "class": self._meta.model_name}

    @property
    def permalink(self) -> str:
        return self.url_node and self.url_node.permalink

    @property
    def routerlink(self) -> str:
        return self.url_node and self.url_node.routerlink

    @property
    def breadcrumbs(self) -> Sequence[dict]:
        breadcrumb = {
            "permalink": self.permalink,
            "title": self.breadcrumbs_title or self.title or self.slug,
        }
        if self.parent:
            return self.parent.breadcrumbs + [breadcrumb]
        return [breadcrumb]

    @property
    def is_public(self) -> bool:
        status = get_nofallbacks(self, "status")
        publication_date = get_nofallbacks(self, "publication_date")
        if status == "PUB":
            return True
        if status == "PLA":
            return bool(publication_date) and timezone.now() > publication_date
        return False

    def get_template_path(self, request=None) -> str:
        return self.template or pointed_getter(self, "_page_meta.default_template")

    @property
    def childs(self) -> models.Manager:
        if hasattr(self._page_meta, "child_page_field"):
            return getattr(self, self._page_meta.child_page_field)
        return getattr(self, PAGE_CHILD_RELATED_NAME % self.model_info)

    @property
    def parent(self) -> models.Model:
        return getattr(self, self._page_meta.parent_page_field)

    def _get_or_create_url_node(self) -> UrlNode:
        if not self.url_node:
            self.url_node = UrlNode.objects.create(
                related_name=URL_NODE_RELATED_NAME % self.model_info
            )
        return self.url_node

    def _update_url_node(self, force: bool = False) -> UrlNode:
        self.url_node = self._get_or_create_url_node()
        for __ in activate_languages():
            old_permalink = self.permalink
            new_permalink = self.generate_permalink()
            force = force or old_permalink != new_permalink
            set_nofallbacks(self.url_node, "permalink", new_permalink)
        if force:
            self.url_node.save()
            self.update_childs()
        return self.url_node

    def generate_permalink(self, safe: bool = True) -> str:
        slug = get_nofallbacks(self, "slug")
        if slug is None and not self.permalink:
            translations = get_field_translations(self, "slug").values()
            fallback_slug = next((t for t in translations if t is not None), None)
            slug = (
                slugify(self.title or uuid4(), allow_unicode=True)
                if fallback_slug is None
                else fallback_slug
            )
            set_nofallbacks(self, "slug", slug)
        permalink = "/%s" % slugify(slug or "", allow_unicode=True)
        if self.parent:
            permalink = f"{self.parent.permalink}{permalink}"
        qs = UrlNode.objects.exclude(pk=getattr(self.url_node or object, "pk", None))
        if safe and qs.filter(permalink=permalink).exists():
            permalink = "/".join(
                permalink.split("/")[:-1] + [slugify(uuid4(), allow_unicode=True)]
            )
        return permalink

    def update_childs(self) -> None:
        # without pk, no childs there
        if self.pk is not None:
            for child in self.childs.all():
                child.save()

    def save(self, *args, **kwargs) -> None:
        with transaction.atomic():
            self._update_url_node()
            return super().save(*args, **kwargs)

    @classmethod
    def get(cls, request, *args, **kwargs) -> "AbstractPage":
        bypass_type_check = kwargs.pop("bypass_type_check", False)
        bypass_public_check = kwargs.pop("bypass_public_check", False)
        path = request.path
        if getattr(django_settings, "APPEND_SLASH", True):
            path = path.rstrip("/")
        if len(kwargs.keys()) > 0:
            page = cls.objects.get(**kwargs)
        else:
            node = UrlNode.objects.filter(
                permalink=url_lang_decompose(path)["permalink"]
            ).first()
            page = node and node.page
        type_error = not bypass_type_check and not isinstance(page, cls)
        public_error = not bypass_public_check and not getattr(
            page or object, "is_public", False
        )
        if not page or type_error or public_error:
            bases = (UrlNode.DoesNotExist,)
            if hasattr(cls, "DoesNotExist"):
                bases += (cls.DoesNotExist,)
            message = "%s matching query does not exist." % cls._meta.object_name
            if public_error:
                message = (
                    "Match found: %s.\nThe page appears not to be public.\nUse ?preview=true in the url to see it."
                    % page
                )
            raise type("PageDoesNotExist", bases, {})(message)
        return page

    @classmethod
    def get_or_create(cls, request, *args, **kwargs) -> Tuple["AbstractPage", bool]:
        try:
            return cls.get(request, *args, **kwargs), False
        except ObjectDoesNotExist:
            if len(kwargs.keys()) > 0:
                return cls.objects.get_or_create(**kwargs)
        return (None, False)

    @classmethod
    def get_or_create_homepage(cls) -> Tuple["AbstractPage", bool]:
        try:
            if settings.ENABLE_TRANSLATIONS:
                node = UrlNode.objects.get(lang_fallback_query(permalink="/"))
            else:
                node = UrlNode.objects.get(permalink="/")
            return node.page, False
        except UrlNode.DoesNotExist:
            return cls.get_or_create(None, slug="")

    @classmethod
    def get_or_404(cls, request, *args, **kwargs) -> "AbstractPage":
        try:
            return cls.get(request, *args, **kwargs)
        except ObjectDoesNotExist as ex:
            raise Http404(ex)

    def alternate_urls(self, *args, **kwargs) -> dict:
        permalinks = get_field_translations(self.url_node or object, "permalink", None)
        for lang in activate_languages():
            if lang in permalinks:
                permalinks[lang] = (
                    UrlNode.reverse_url(permalinks[lang]) if self.is_public else None
                )
        return permalinks

    class Meta:
        abstract = True
        ordering = ("ordering",)
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    class PageMeta:
        parent_page_field = "parent_page"
        default_template = settings.PAGE_DEFAULT_TEMPLATE
        inject_context_func = settings.PAGE_INJECT_CONTEXT_FUNC


class Page(AbstractPage):
    pass


@receiver(post_delete)
def auto_delete_url_node(sender, instance, **kwargs):
    if issubclass(sender, AbstractPage):
        instance.url_node and instance.url_node.delete()
