# Generated by Django 2.2.27 on 2022-03-09 16:16

import camomilla.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("camomilla", "0007_auto_20220211_1622"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ["ordering"]},
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["ordering"], "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="page",
            options={
                "ordering": ["ordering"],
                "verbose_name": "Page",
                "verbose_name_plural": "Pages",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="meta",
            field=camomilla.fields.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="article",
            name="ordering",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="category",
            name="meta",
            field=camomilla.fields.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="category",
            name="ordering",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="page",
            name="meta",
            field=camomilla.fields.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="page",
            name="ordering",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
