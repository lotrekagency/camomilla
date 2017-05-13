import os

import uuid
import json

from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from hvad.models import TranslatableModel, TranslatedFields


def create_content_id():
  return str(uuid.uuid4())[0:8]


CONTENT_STATUS = (
    ('PUB', _('Published')),
    ('DRF', _('Draft')),
    ('TRS', _('Trash')),
)


PERMISSION_LEVELS = (
    ('1', _('Guest')),
    ('2', _('Editor')),
    ('3', _('Admin')),
)


class SlugMixin(object):

    slug_attr = 'title'

    def get_slug(self):
        return self.slug

    get_slug.short_description = _('Slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(getattr(self, self.slug_attr))
        super(SlugMixin, self).save(*args, **kwargs)


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


class BaseArticle(TranslatableModel, SlugMixin):
    identifier = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
        description = models.TextField(blank=True, null=True, default=''),
        permalink = models.SlugField(max_length=200),
        og_description = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_title = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_type = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_url = models.CharField(max_length=200, blank=True, null=True, default=''),
        canonical = models.CharField(max_length=200, blank=True, null=True, default=''),
        slug = models.SlugField(blank=True)
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    highlight_image = models.ForeignKey('camomilla.Media', blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('camomilla.Tag', blank=True)
    categories = models.ManyToManyField('camomilla.Category', blank=True)
    og_image = models.ImageField(blank=True, null=True, default='')

    class Meta:
        abstract = True
        unique_together = [('permalink', 'language_code')]
        permissions = (
            ("read_article", _("Can read article")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Article(BaseArticle):
    translations = TranslatedFields()


class BaseContent(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        subtitle = models.CharField(max_length=200, blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200, blank=True, null=True),
        content = models.TextField()
    )
    identifier = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    date = models.DateTimeField(auto_now=True)
    page = models.ForeignKey('camomilla.SitemapUrl', blank=False, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        unique_together = [('page', 'identifier')]
        permissions = (
            ("read_content", _("Can read content")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Content(BaseContent):
    translations = TranslatedFields()


class BaseTag(SlugMixin, TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        slug = models.SlugField(blank=True)
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
        title = models.CharField(max_length=200, unique=True)
    )

    class Meta:
        abstract = True
        verbose_name_plural = "categories"
        permissions = (
            ("read_category", _("Can read category")),
        )

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Category(BaseCategory):
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

    def image_preview(self):
        if self.is_image and self.file:
            return mark_safe('<img src="{0}" />'.format(self.file.url))

    def image_thumb_preview(self):
        if self.is_image and self.thumbnail:
            return mark_safe('<img src="{0}" />'.format(self.thumbnail.url))

    image_preview.short_description = _('Preview')
    image_thumb_preview.short_description = _('Thumbnail')

    class Meta:
        permissions = (
            ("read_media", _("Can read media")),
        )
        ordering = ['-created']


    def __init__(self, *args, **kwargs):
        super(Media, self).__init__(*args, **kwargs)
        self.__original_file = self.file

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
        self.__original_file = self.file
        from PIL import Image
        import os
        from django.core.files.base import ContentFile

        from django.core.files.storage import default_storage as storage

        from io import BytesIO

        try:
            fh = storage.open(self.file.name, 'rb')
        except FileNotFoundError:
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

    def _optimize(self):
        opt_command = settings.OPTIMIZATION_COMMAND.format(self.file.name)
        os.system(opt_command)

    def save(self, *args, **kwargs):
        if self.file != self.__original_file or not self.pk:
            self._make_thumbnail()
        if self.file:
            self.size = self.file.size
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name
        return self.file.name


class BaseSitemapUrl(TranslatableModel):
    page = models.CharField(max_length=200, unique=True)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200, blank=True),
        og_description = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_title = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_type = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_url = models.CharField(max_length=200, blank=True, null=True, default=''),
        canonical = models.CharField(max_length=200, blank=True, null=True, default=''),
    )
    og_image = models.ImageField(blank=True, null=True, default='')

    class Meta:
        abstract = True
        permissions = (
            ("read_sitemapurl", _("Can read sitemap url")),
        )

    def __str__(self):
        return self.page


class SitemapUrl(BaseSitemapUrl):
    translations = TranslatedFields()
