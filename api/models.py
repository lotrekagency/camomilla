from __future__ import unicode_literals
from django.conf import settings

from django.db import models


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    level = models.CharField(
        max_length=3,
        choices=PERMISSION_LEVELS,
        default='1',
    )


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    status = models.CharField(
        max_length=3,
        choices=CONTENT_STATUS,
        default='DRF',
    )
    date = models.DateTimeField(auto_now=True)


class Language(models.Model):
    sign = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=200)

