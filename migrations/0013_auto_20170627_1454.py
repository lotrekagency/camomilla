# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-27 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0012_mediatranslation_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['-pk'], 'permissions': (('read_media', 'Can read media'),)},
        ),
    ]