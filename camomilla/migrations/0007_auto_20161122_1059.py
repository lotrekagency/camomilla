# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0006_auto_20161121_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='dimension',
            new_name='size',
        ),
    ]
