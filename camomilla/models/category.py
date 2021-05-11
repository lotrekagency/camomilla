from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class BaseCategory(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(blank=True, null=True, default=""),
        slug=models.SlugField(),
    )

    class Meta:
        abstract = True
        unique_together = [("title", "language_code")]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Category(BaseCategory):
    translations = TranslatedFields()
