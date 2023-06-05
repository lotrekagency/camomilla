# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-10-03 08:56
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from camomilla.models import Article


def migrate_title(apps, schema_editor):
    try:
        language_list = [lan[0] for lan in settings.LANGUAGES]
        for language in language_list:
            for instance in Article.objects.language(language).fallbacks().all().iterator():
                instance.content_title = instance.title
                instance.save()
    except Exception as ex: print(ex)


def reverse_migrate_title(apps, schema_editor):
    try:
        language_list = [lan[0] for lan in settings.LANGUAGES]
        for language in language_list:
            for instance in Article.objects.language(language).fallbacks().all().iterator():
                instance.title = instance.content_title
                instance.save()
    except Exception as ex: print(ex)


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0022_auto_20181002_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='trash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='content_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE;'),
        migrations.RunPython(migrate_title, reverse_migrate_title),
        migrations.RunSQL('SET CONSTRAINTS ALL DEFERRED;'),
        migrations.RemoveField(
            model_name='article',
            name='trash',
        )
    ]