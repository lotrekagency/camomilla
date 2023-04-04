import json
import os
import magic
from io import BytesIO

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.db import models
from django.db.models.fields.related import ForeignObjectRel
from ..fields import JSONField
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields
from PIL import Image


class BaseMediaFolder(TranslatableModel):
    translations = TranslatedFields(
        description=models.CharField(max_length=200, blank=True, null=True),
        title=models.CharField(max_length=200, blank=True, null=True),
    )
    slug = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    icon = models.ForeignKey(
        "camomilla.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Image cover"),
    )
    path = models.TextField(blank=True, null=True)
    updir = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child_folders",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def update_childs(self):
        for folder in self.child_folders.all():
            folder.save()

    def save(self, *args, **kwargs):
        if self.updir:
            if self.updir.id == self.id:
                raise ValidationError({"updir": "Unvalid parent"})
            self.path = "{0}/{1}".format(self.updir.path, self.slug)

        else:
            self.path = "/{0}".format(self.slug)

        super(BaseMediaFolder, self).save(*args, **kwargs)
        self.update_childs()

    def __str__(self):
        to_string = self.slug
        if self.title:
            to_string += " - " + self.title
        return to_string


class MediaFolder(BaseMediaFolder):
    translations = TranslatedFields()


class Media(TranslatableModel):
    translations = TranslatedFields(
        alt_text=models.CharField(max_length=200, blank=True, null=True),
        title=models.CharField(max_length=200, blank=True, null=True),
        description=models.TextField(blank=True, null=True),
    )
    file = models.FileField()
    thumbnail = models.ImageField(
        upload_to=getattr(settings, "THUMB_FOLDER", "thumbnails"),
        max_length=500,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    size = models.IntegerField(default=0, blank=True, null=True)
    mime_type = models.CharField(max_length=128, blank=True, null=True)
    image_props = JSONField(default=dict, blank=True)
    folder = models.ForeignKey(
        MediaFolder,
        null=True,
        blank=True,
        related_name="media_folder",
        on_delete=models.CASCADE,
    )

    @property
    def path(self):
        return "%s/%s" % (self.folder.path, self.name)

    @property
    def is_image(self):
        return self.mime_type and self.mime_type.startswith("image")

    def image_preview(self):
        if self.file:
            return mark_safe('<img src="{0}" />'.format(self.file.url))

    def image_thumb_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{0}" />'.format(self.thumbnail.url))

    image_preview.short_description = _("Preview")
    image_thumb_preview.short_description = _("Thumbnail")

    class Meta:
        ordering = ["-pk"]

    def regenerate_thumbnail(self):
        if self.file:
            self._make_thumbnail()

    def get_foreign_fields(self):
        return [
            field.get_accessor_name()
            for field in self._meta.get_fields()
            if issubclass(type(field), ForeignObjectRel)
        ]

    @property
    def json_repr(self):
        json_r = {
            "id": self.pk,
            "thumbnail": "" if not self.is_image else self.thumbnail.url,
            "label": self.__str__(),
        }
        return json.dumps(json_r)

    def _make_thumbnail(self):
        try:
            fh = storage.open(self.file.name, "rb")
            self.mime_type = magic.from_buffer(fh.read(2048), mime=True)
        except FileNotFoundError as ex:
            print(ex)
            self.image_props = {}
            self.mime_type = ""
            return False
        try:
            orig_image = Image.open(fh)
            image = orig_image.copy()
            self.image_props = {
                "width": orig_image.width,
                "height": orig_image.height,
                "format": orig_image.format,
                "mode": orig_image.mode,
            }
        except Exception as ex:
            print(ex)
            return False

        try:
            image.thumbnail(
                (
                    getattr(settings, "CAMOMILLA_THUMBNAIL_WIDTH", 50),
                    getattr(settings, "CAMOMILLA_THUMBNAIL_HEIGHT", 50),
                ),
                Image.ANTIALIAS,
            )
            fh.close()

            # Path to save to, name, and extension
            thumb_name, thumb_extension = os.path.splitext(self.file.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + "_thumb" + thumb_extension

            temp_thumb = BytesIO()
            image.save(temp_thumb, "PNG", optimize=True)
            temp_thumb.seek(0)

            # Load a ContentFile into the thumbnail field so it gets saved
            self.thumbnail.save(
                thumb_filename, ContentFile(temp_thumb.read()), save=False
            )
            temp_thumb.close()
        except Exception:
            return False

        return True

    def _remove_file(self):
        if self.file:
            file_to_remove = os.path.join(settings.MEDIA_ROOT, self.file.name)
            if os.path.isfile(file_to_remove):
                os.remove(file_to_remove)

    def _remove_thumbnail(self):
        if self.thumbnail:
            file_to_remove = os.path.join(settings.MEDIA_ROOT, self.thumbnail.name)
            if os.path.isfile(file_to_remove):
                os.remove(file_to_remove)

    def _get_file_size(self):
        if self.file:
            file_to_calc = os.path.join(settings.MEDIA_ROOT, self.file.name)
            if os.path.isfile(file_to_calc):
                return self.file.size
            else:
                return 0

    def __str__(self):
        if self.name:
            return self.name
        return self.file.name


@receiver(post_save, sender=Media, dispatch_uid="make thumbnails")
def update_media(sender, instance, **kwargs):
    instance._remove_thumbnail()
    instance._make_thumbnail()
    Media.objects.filter(pk=instance.pk).update(
        size=instance._get_file_size(),
        thumbnail=instance.thumbnail,
        mime_type=instance.mime_type,
        image_props=instance.image_props,
    )


@receiver(pre_delete, sender=Media, dispatch_uid="make thumbnails")
def delete_media_files(sender, instance, **kwargs):
    instance._remove_thumbnail()
    instance._remove_file()
