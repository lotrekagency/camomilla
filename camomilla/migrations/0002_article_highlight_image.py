# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='highlight_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='camomilla.Media'),
        ),
    ]
