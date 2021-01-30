# Generated by Django 2.2.17 on 2021-01-30 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0002_auto_20200214_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafolder',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mediafolder',
            name='updir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_folders', to='camomilla.MediaFolder'),
        ),
    ]
