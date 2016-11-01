from __future__ import unicode_literals
from django.conf import settings

from django.db import models

from hvad.models import TranslatableModel, TranslatedFields


CONTENT_STATUS = (
    ('PUB', 'Published'),
    ('DRF', 'Draft'),
    ('TRS', 'Trash'),
)


PERMISSION_LEVELS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    level = models.CharField(
        max_length=3,
        choices=PERMISSION_LEVELS,
        default='1',
    )


class Article(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
        description = models.TextField(blank=True, null=True, default=''),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    permalink = models.CharField(max_length=200, unique=True)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=True, null=True)
    canonical = models.CharField(max_length=200, blank=True, null=True, default='')
    robots = models.CharField(max_length=200, blank=True, null=True, default='')
    og_image = models.CharField(max_length=200, blank=True, null=True, default='')
    og_description = models.CharField(max_length=200, blank=True, null=True, default='')
    og_title = models.CharField(max_length=200, blank=True, null=True, default='')
    og_type = models.CharField(max_length=200, blank=True, null=True, default='')
    og_url = models.CharField(max_length=200, blank=True, null=True, default='')


class Content(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        subtitle = models.CharField(max_length=200, blank=True, null=True, default=''),
        content = models.TextField(),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    permalink = models.CharField(max_length=200, unique=True)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    date = models.DateTimeField(auto_now=True)


class Tag(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, unique=True)
    )

    def __str__(self):
        return self.safe_translation_getter('title', str(self.pk))


class Category(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, unique=True)
    )


class Media(models.Model):
    file = models.FileField()
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    dimension = models.IntegerField(default=0, blank=True, null=True)


class SitemapUrl(models.Model):
    url = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    canonical = models.CharField(max_length=200, blank=True, null=True, default='')
    robots = models.CharField(max_length=200, blank=True, null=True, default='')
    og_image = models.CharField(max_length=200, blank=True, null=True, default='')
    og_description = models.CharField(max_length=200, blank=True, null=True, default='')
    og_title = models.CharField(max_length=200, blank=True, null=True, default='')
    og_type = models.CharField(max_length=200, blank=True, null=True, default='')
    og_url = models.CharField(max_length=200, blank=True, null=True, default='')
