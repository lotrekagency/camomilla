from django.db import models
from hvad.models import TranslatedFields
from .mixins import SeoMixin, MetaMixin
from ..utils import get_page


class BasePage(SeoMixin, MetaMixin):
    identifier = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields()
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["ordering"]

    @classmethod
    def get(model, request, **kwargs):
        return get_page(request, **kwargs)

    def alternate_urls(self, request):
        from djlotrek.context_processors import alternate_seo_url

        return alternate_seo_url(request)

    def __str__(self):
        return self.identifier


class Page(BasePage):
    translations = TranslatedFields()
