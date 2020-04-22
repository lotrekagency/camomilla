# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0017_auto_20171127_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('title', 'language_code'), ('language_code', 'master')]),
        ),
    ]
