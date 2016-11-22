from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from hvad.models import TranslatableModel, TranslatedFields


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


class BaseUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )
    level = models.CharField(
        max_length=3,
        choices=PERMISSION_LEVELS,
        default='1',
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class UserProfile(BaseUserProfile):
    pass


def create_user_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        level = '1'
        if user.is_superuser:
            level = '3'
        profile = UserProfile(user=user, level=level)
        profile.save()


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)


class Page(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class BaseArticle(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
        description = models.TextField(blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200),
        og_description = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_title = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_type = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_url = models.CharField(max_length=200, blank=True, null=True, default=''),
        canonical = models.CharField(max_length=200, blank=True, null=True, default='')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    highlight_image = models.ForeignKey('camomilla.Media', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('camomilla.Tag', blank=True)
    categories = models.ManyToManyField('camomilla.Category', blank=True)
    og_image = models.CharField(max_length=200, blank=True, null=True, default='')

    class Meta:
        abstract = True
        unique_together = [('permalink', 'language_code')]

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Article(BaseArticle):
    translations = TranslatedFields()


class BaseContent(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        subtitle = models.CharField(max_length=200, blank=True, null=True, default=''),
        content = models.TextField(),
        permalink = models.CharField(max_length=200)
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    date = models.DateTimeField(auto_now=True)
    page = models.ForeignKey('camomilla.Page', blank=False, null=True)

    class Meta:
        unique_together = [('permalink', 'language_code')]
        abstract = True

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Content(BaseContent):
    translations = TranslatedFields()


class BaseTag(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, unique=True)
    )

    class Meta:
        abstract = True

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

    def __str__(self):
        return self.lazy_translation_getter('title', str(self.pk))


class Category(BaseCategory):
    translations = TranslatedFields()


class Media(TranslatableModel):
    translations = TranslatedFields(
        alt_text = models.CharField(max_length=200, blank=True, null=True),
        title = models.CharField(max_length=200, blank=True, null=True)
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
    dimension = models.IntegerField(default=0, blank=True, null=True)
    is_image = models.BooleanField(default=False)

    def _make_thumbnail(self):
        from PIL import Image
        import os
        from django.core.files.base import ContentFile

        from django.core.files.storage import default_storage as storage

        from io import BytesIO

        fh = storage.open(self.file.name, 'rb')
        try:
            image = Image.open(fh)
            self.is_image = True
        except Exception as ex:
            print (ex)
            return False

        image.thumbnail((50, 50), Image.ANTIALIAS)
        fh.close()

        # Path to save to, name, and extension
        thumb_name, thumb_extension = os.path.splitext(self.file.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        temp_thumb = BytesIO()
        image.save(temp_thumb, 'PNG')
        temp_thumb.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved
        print (thumb_filename)
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=True)
        temp_thumb.close()

        return True

    def save(self, *args, **kwargs):
        super(Media, self).save()
        if self.file and not self.dimension:
            self.dimension = self.file.size
            self.save()
        if not self.thumbnail:
            self._make_thumbnail()

    def __str__(self):
        return self.file.name


class BaseSitemapUrl(TranslatableModel):

    url = models.CharField(max_length=200, unique=True)
    page = models.ForeignKey('camomilla.Page', blank=False, null=True)
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200),
        og_description = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_title = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_type = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_url = models.CharField(max_length=200, blank=True, null=True, default=''),
        canonical = models.CharField(max_length=200, blank=True, null=True, default=''),
    )
    og_image = models.CharField(max_length=200, blank=True, null=True, default='')

    class Meta:
        abstract = True


class SitemapUrl(BaseSitemapUrl):
    translations = TranslatedFields()
