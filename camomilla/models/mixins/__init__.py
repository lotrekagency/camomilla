from django.db import models
from ...fields import JSONField
from hvad.models import TranslatableModel, TranslatedFields

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from ...utils import get_seo_model

from djlotrek.utils import alternate_seo_url_with_object


class SeoMixin(TranslatableModel):

    seo_attr = "identifier"

    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(blank=True, null=True, default=""),
        permalink=models.CharField(max_length=200, blank=True),
        og_description=models.TextField(blank=True, null=True, default=""),
        og_title=models.CharField(max_length=200, blank=True, null=True, default=""),
        og_type=models.CharField(max_length=200, blank=True, null=True, default=""),
        og_url=models.CharField(max_length=200, blank=True, null=True, default=""),
        canonical=models.CharField(max_length=200, blank=True, null=True, default=""),
    )
    og_image = models.ForeignKey(
        "camomilla.Media",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
    )

    @classmethod
    def get(model, request, **kwargs):
        return get_seo_model(request, model, **kwargs)

    def alternate_urls(self, request):
        return alternate_seo_url_with_object(
            request, self.__class__, permalink=self.permalink
        )

    class Meta:
        abstract = True


class SlugMixin(object):

    slug_attr = "title"

    def get_slug(self):
        return self.slug

    get_slug.short_description = _("Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(getattr(self, self.slug_attr))
        super(SlugMixin, self).save(*args, **kwargs)


class MetaMixin(models.Model):
    meta = JSONField(default=dict)

    def get_meta(self, key, default=None):
        return self.meta.get(key, default)

    def update_meta(self, key, value):
        self.meta[key] = value
        super(MetaMixin, self).save(update_fields=["meta"])

    def delete_meta(self, key):
        del self.meta[key]
        super(MetaMixin, self).save(update_fields=["meta"])

    class Meta:
        abstract = True
