from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from .mixins import MetaMixin


class BaseCategory(TranslatableModel, MetaMixin):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(blank=True, null=True, default=""),
        slug=models.SlugField(),
    )
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        unique_together = [("title", "language_code")]
        verbose_name_plural = "categories"
        ordering = ["ordering"]

    def __str__(self):
        return self.title


class Category(BaseCategory):
    translations = TranslatedFields()
