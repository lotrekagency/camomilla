# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 12:34
from __future__ import unicode_literals

import camomilla.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='identifier',
            field=models.CharField(default=camomilla.models.create_content_id, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='contenttranslation',
            name='permalink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]