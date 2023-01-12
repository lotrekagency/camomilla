from django.db import models
from .mixins import MetaMixin


class BaseCategory(MetaMixin):
    title=models.CharField(max_length=200, null=True)
    description=models.TextField(blank=True, null=True, default="")
    slug=models.SlugField(null=True, unique=True)
    ordering = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        verbose_name_plural = "categories"
        ordering = ["ordering"]

    def __str__(self):
        return self.title


class Category(BaseCategory):
    pass