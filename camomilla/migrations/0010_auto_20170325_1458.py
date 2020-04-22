# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-25 14:58
from __future__ import unicode_literals

import camomilla.models

from django.db import migrations, models


def set_articles_identifier(apps, schema_editor):
    Article = apps.get_model("camomilla", "Article")
    for article in Article.objects.all():
        article.identifier = camomilla.models.create_content_id()
        article.save()

def unset_articles_identifier(apps, schema_editor):
    Article = apps.get_model("camomilla", "Article")
    for article in Article.objects.all():
        article.indentifier = ''
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0009_auto_20170325_1456'),
    ]

    operations = [
        migrations.RunPython(
            set_articles_identifier,
            unset_articles_identifier
        ),
    ]
