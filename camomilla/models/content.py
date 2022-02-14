from django.db import models

from django.urls import reverse

from hvad.models import TranslatableModel, TranslatedFields

from djsuperadmin.mixins import DjSuperAdminMixin


class BaseContent(DjSuperAdminMixin, TranslatableModel):
    identifier = models.CharField(max_length=200)
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        subtitle=models.CharField(max_length=200, blank=True, null=True, default=""),
        permalink=models.CharField(max_length=200, blank=False, null=True),
        content=models.TextField(default=""),
    )
    page = models.ForeignKey(
        "camomilla.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="contents",
    )

    @property
    def superadmin_get_url(self):
        return reverse("camomilla-content-djsuperadmin", kwargs={"pk": self.pk})

    @property
    def superadmin_patch_url(self):
        return reverse("camomilla-content-djsuperadmin", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
        unique_together = [("page", "identifier")]

    def __str__(self):
        return self.identifier


class Content(BaseContent):
    translations = TranslatedFields()
