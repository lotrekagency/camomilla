import os

import uuid
import json

from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from hvad.models import TranslatableModel, TranslatedFields

from subprocess import Popen
from .mixins import SeoMixin, SlugMixin


def create_content_id():
  return str(uuid.uuid4())[0:8]


CONTENT_STATUS = (
    ('PUB', _('Published')),
    ('DRF', _('Draft')),
    ('TRS', _('Trash')),
    ('PLA', _('Planned')),
)


PERMISSION_LEVELS = (
    ('1', _('Guest')),
    ('2', _('Editor')),
    ('3', _('Admin')),
)


class CamomillaBaseUser(AbstractUser):
    level = models.CharField(
        max_length=3,
        choices=PERMISSION_LEVELS,
        default='1',
    )
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):

        try:
            orig = self.__class__.objects.get(pk=self.pk)
        except:
            orig = None

        super(CamomillaBaseUser, self).save()
        if orig and orig.level == self.level:
            return self

        if self.level == '1':
            permissions = Permission.objects.filter(
                Q(content_type__app_label__contains='camomilla') |
                Q(content_type__app_label__contains='plugin_'),
                codename__contains='read'
            )
            for permission in permissions:
                self.user_permissions.add(permission)

        if self.level == '2':
            permissions = Permission.objects.filter(
                Q(content_type__app_label__contains='camomilla') |
                Q(content_type__app_label__contains='plugin_')
            )
            for permission in permissions:
                self.user_permissions.add(permission)

        if self.level == '3':
            permissions = Permission.objects.filter(
                Q(content_type__app_label__contains='camomilla') |
                Q(content_type__app_label__contains='plugin_') |
                Q(content_type__model='token') |
                Q(content_type__model='user')
            )
            for permission in permissions:
                self.user_permissions.add(permission)

    class Meta:
        abstract = True
        permissions = (
            ("read_userprofile", _("Can read user profile")),
        )


class BaseArticle(SeoMixin):

    seo_attr = 'permalink'

    identifier = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields(
        content_title = models.CharField(max_length=200),
        content = models.TextField(),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    highlight_image = models.ForeignKey('camomilla.Media', blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now=True)
    pubblication_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('camomilla.Tag', blank=True)
    categories = models.ManyToManyField('camomilla.Category', blank=True)

    class Meta:
        abstract = True
        unique_together = [('permalink', 'language_code')]
        permissions = (
            ("read_article", _("Can read article")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Article(BaseArticle):
    translations = TranslatedFields()


class BaseContent(TranslatableModel):
    identifier = models.CharField(max_length=200)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        subtitle = models.CharField(max_length=200, blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200, blank=True, null=True),
        content = models.TextField()
    )
    page = models.ForeignKey('camomilla.SitemapUrl', blank=False, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        unique_together = [('page', 'identifier')]
        permissions = (
            ("read_content", _("Can read content")),
        )

    def __str__(self):
        return self.page.identifier + " > " + self.identifier


class Content(BaseContent):
    translations = TranslatedFields()


class BaseTag(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
    )

    class Meta:
        abstract = True
        unique_together = [('title', 'language_code')]
        permissions = (
            ("read_tag", _("Can read tag")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Tag(BaseTag):
    translations = TranslatedFields()


class BaseCategory(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True, default=''),
        slug = models.SlugField()
    )

    class Meta:
        abstract = True
        unique_together = [('title', 'language_code')]
        verbose_name_plural = "categories"
        permissions = (
            ("read_category", _("Can read category")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Category(BaseCategory):
    translations = TranslatedFields()


class BaseSitemapUrl(SeoMixin):
    identifier = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields()

    class Meta:
        abstract = True
        permissions = (
            ("read_sitemapurl", _("Can read sitemap url")),
        )
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.identifier


class SitemapUrl(BaseSitemapUrl):
    translations = TranslatedFields()


Page = SitemapUrl


from PIL import Image
import os
from django.core.files.base import ContentFile

from django.core.files.storage import default_storage as storage

from io import BytesIO

class BaseMediaFolder(TranslatableModel):
    translations = TranslatedFields(
        description = models.CharField(max_length=200, blank=True, null=True),
        title = models.CharField(max_length=200, blank=True, null=True),
    )
    slug = models.SlugField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    icon = models.ForeignKey('camomilla.Media', on_delete=models.SET_NULL,
                              null=True, blank=True,  verbose_name=_('Image cover'))
    updir = models.ForeignKey('self', on_delete=models.CASCADE,
                                 null=True, blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        to_string = self.slug
        if self.title:
            to_string+=" - "+self.title
        return to_string


class MediaFolder(BaseMediaFolder):
    translations = TranslatedFields()

class Media(TranslatableModel):
    translations = TranslatedFields(
        alt_text = models.CharField(max_length=200, blank=True, null=True),
        title = models.CharField(max_length=200, blank=True, null=True),
        description = models.TextField(blank=True, null=True)
    )
    file = models.FileField()
    thumbnail = models.ImageField(
        upload_to=settings.THUMB_FOLDER,
        max_length=500,
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    size = models.IntegerField(default=0, blank=True, null=True)
    is_image = models.BooleanField(default=False)
    folder = models.ForeignKey(MediaFolder, null=True, blank=True, related_name="media_folder")
    def image_preview(self):
        if self.file:
            return mark_safe('<img src="{0}" />'.format(self.file.url))

    def image_thumb_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{0}" />'.format(self.thumbnail.url))

    image_preview.short_description = _('Preview')
    image_thumb_preview.short_description = _('Thumbnail')

    class Meta:
        permissions = (
            ("read_media", _("Can read media")),
        )
        ordering = ['-pk']

    def regenerate_thumbnail(self):
        if self.file:
            self._make_thumbnail()

    def optimize(self):
        if self.file:
            self._optimize()

    @property
    def json_repr(self):
        json_r = {
            'id': self.pk,
            'thumbnail': '' if not self.is_image else self.thumbnail.url,
            'label': self.__str__()
        }
        return json.dumps(json_r)

    def _make_thumbnail(self):

        try:
            fh = storage.open(self.file.name, 'rb')
        except FileNotFoundError as ex:
            print (ex)
            self.is_image = False
            return False
        try:
            orig_image = Image.open(fh)
            image = orig_image.copy()
            self.is_image = True
        except Exception as ex:
            print (ex)
            return False

        image.thumbnail(
            (settings.CAMOMILLA_THUMBNAIL_WIDTH, settings.CAMOMILLA_THUMBNAIL_HEIGHT),
            Image.ANTIALIAS
        )
        fh.close()

        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.file.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        temp_thumb = BytesIO()
        image.save(temp_thumb, 'PNG', optimize=True)
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def _optimize_command(self):

        try:
            fh = storage.open(self.file.name, 'rb')
        except FileNotFoundError as ex:
            return ''
        try:
            my_image = Image.open(fh)
        except Exception as ex:
            print (ex)
            return ''

        if my_image.format == 'JPEG':
            opt_command = settings.JPEG_OPTIMIZATION_COMMAND.format(
                os.path.join(settings.MEDIA_ROOT, self.file.name)
            )
            return opt_command
        elif my_image.format == 'PNG':
            opt_command = settings.PNG_OPTIMIZATION_COMMAND.format(
                os.path.join(settings.MEDIA_ROOT, self.file.name)
            )
            return opt_command
        else:
            return ''

    def _optimize(self):
        opt_command = self._optimize_command()
        os.system(opt_command)

    def _optimize_async(self):
        opt_command = self._optimize_command()
        try:
            p = Popen(opt_command, shell=True)
        except FileNotFoundError as ex:
            print (ex)

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
        is_image=instance.is_image
    )
    instance._optimize_async()


@receiver(pre_delete, sender=Media, dispatch_uid="make thumbnails")
def delete_media_files(sender, instance, **kwargs):
    instance._remove_thumbnail()
    instance._remove_file()
