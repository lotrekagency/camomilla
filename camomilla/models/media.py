import json
import base64
import os
from io import BytesIO
import cv2
from django.template import Template, Context

import magic
from django.conf import settings
from camomilla.settings import (
    THUMBNAIL_WIDTH,
    THUMBNAIL_HEIGHT,
    THUMBNAIL_FOLDER,
    MEDIA_MAX_WIDTH,
    MEDIA_MAX_HEIGHT,
    MEDIA_DPI,
    MEDIA_BREAKPOINTS,
)
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.db import models
from django.db.models.fields.related import ForeignObjectRel
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image

from camomilla.fields import JSONField


class AbstractMediaFolder(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, max_length=200, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
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
        self.slug = slugify(self.title)
        if self.updir:
            if self.updir.id == self.id:
                raise ValidationError({"updir": "Unvalid parent"})
            self.path = "{0}/{1}".format(self.updir.path, self.slug)
        else:
            self.path = "/{0}".format(self.slug)

        super().save(*args, **kwargs)
        self.update_childs()

    def __str__(self):
        return "[%s] %s" % (self.__class__.__name__, self.name)


class MediaFolder(AbstractMediaFolder):
    pass


class Media(models.Model):
    # Seo Attributes
    alt_text = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    file = models.FileField()
    thumbnail = models.ImageField(
        upload_to=THUMBNAIL_FOLDER,
        max_length=500,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now=True)
    size = models.IntegerField(default=0, blank=True, null=True)
    mime_type = models.CharField(max_length=128, blank=True, null=True)
    image_props = JSONField(default=dict, blank=True)
    image_sourceset = JSONField(default=dict, blank=True)
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


    def image_thumb_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{0}" />'.format(self.thumbnail.url))

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
        return self._resize(thumbnail=True)

    def _identify_relevant_area(self):
        image = cv2.imread(self.file.path)
        gray_scale_version = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(
            gray_scale_version, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        contours, _ = cv2.findContours(
            threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest_contour)

        center_x = x + w // 2
        center_y = y + h // 2
        center_x = int(center_x / image.shape[1]*100)
        center_y = int(center_y / image.shape[0]*100)
        
        return {"center_x": f"{center_x}%", "center_y": f"{center_y}%"}

    def _resize(self, thumbnail=False, breakpoint=None):
        try:
            fh = storage.open(self.file.name, "rb")
            self.mime_type = magic.from_buffer(fh.read(2048), mime=True)
        except FileNotFoundError as ex:
            self.image_props = {}
            self.mime_type = ""
            return False, {}
        try:
            image = Image.open(fh)
            self.image_props = {
                "width": image.width,
                "height": image.height,
                "format": image.format,
                "mode": image.mode,
            }
        except Exception as ex:
            print(ex)
            return False, {}

        try:
            image_sourceset = {}
            if thumbnail:
                image.thumbnail((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT), Image.ANTIALIAS)
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

            else:
                width, height = image.size


                if width <= height:
                    selected_width = int((MEDIA_MAX_HEIGHT / height) * width)
                    selected_height = MEDIA_MAX_HEIGHT
                else:
                    selected_height = int((MEDIA_MAX_WIDTH / width) * height)
                    selected_width = MEDIA_MAX_WIDTH

                image = image.resize([selected_width, selected_height], resample=Image.LANCZOS)

                image.info["dpi"] = (MEDIA_DPI, MEDIA_DPI)
                self.image_props = {
                    "width": image.width,
                    "height": image.height,
                    "format": image.format,
                    "mode": image.mode,
                }

                for breakpoint_name, breakpoint in MEDIA_BREAKPOINTS.items():
                    if width <= height:
                        breakpoint_selected_width = int((breakpoint / height) * width)
                        breakpoint_selected_height = breakpoint
                    else:
                        breakpoint_selected_height = int((breakpoint / width) * height)
                        breakpoint_selected_width = breakpoint
                    breakpoint_image = image.copy()
                    breakpoint_image = breakpoint_image.resize([breakpoint_selected_width, breakpoint_selected_height], resample=Image.LANCZOS) 
                    path = "/".join(self.file.path.split("/")[:-1])
                    file_name, file_extension = os.path.splitext(self.file.name)
                    new_file_name = f"{file_name}-{breakpoint_name}{file_extension}"                    
                    file_path = f"{path}/{file_name}-{breakpoint_name}{file_extension}"
                    breakpoint_image.save(file_path, "PNG", dpi=(MEDIA_DPI, MEDIA_DPI), optimize=True)
                    image_sourceset[breakpoint_name] = self.file.storage.url(new_file_name)

                self.image_sourceset.update(image_sourceset)
                temp_img = BytesIO()
                image.save(temp_img, "PNG", dpi=(MEDIA_DPI, MEDIA_DPI), optimize=True)
                temp_img.seek(0)
                self.file.storage.delete(self.file.name)
                self.file.save(self.file.name, ContentFile(temp_img.read()), save=False)

                temp_img.close()

            fh.close()
            return True, image_sourceset

        except Exception as e:
            print(e)
            return False, {}


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
        return self.file.name


@receiver(post_save, sender=Media, dispatch_uid="make thumbnails")
def update_media(sender, instance, **kwargs):
    center_x, center_y = instance.image_props.get("center_x", None), instance.image_props.get("center_y", None)
    instance._remove_thumbnail()
    _, image_sourceset = instance._resize(thumbnail=False)
    instance._make_thumbnail()
    center_coordinates = {}
    if center_x and center_y:
        center_coordinates['center_x'] = center_x
        center_coordinates['center_y'] = center_y
    else:
        center_coordinates = instance._identify_relevant_area()
    props = {**instance.image_props, **center_coordinates}

    Media.objects.filter(pk=instance.pk).update(
        size=instance._get_file_size(),
        thumbnail=instance.thumbnail,
        mime_type=instance.mime_type,
        image_props=props,
        image_sourceset=image_sourceset,
    )


@receiver(pre_delete, sender=Media, dispatch_uid="make thumbnails")
def delete_media_files(sender, instance, **kwargs):
    instance._remove_thumbnail()
    instance._remove_file()
