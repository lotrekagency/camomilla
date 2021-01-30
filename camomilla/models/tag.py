from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class BaseTag(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
    )

    class Meta:
        abstract = True
        unique_together = [("title", "language_code")]

    def __str__(self):
        return self.title


class Tag(BaseTag):
    translations = TranslatedFields()
