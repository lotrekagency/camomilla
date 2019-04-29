# Generated by Django 2.1.7 on 2019-03-04 14:11

from django.db import migrations, models
import django.db.models.deletion
import hvad.fields


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0026_auto_20181114_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.Article', 'camomilla.ArticleTranslation'),
        ),
        migrations.AddField(
            model_name='category',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.Category', 'camomilla.CategoryTranslation'),
        ),
        migrations.AddField(
            model_name='content',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.Content', 'camomilla.ContentTranslation'),
        ),
        migrations.AddField(
            model_name='media',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.Media', 'camomilla.MediaTranslation'),
        ),
        migrations.AddField(
            model_name='mediafolder',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.MediaFolder', 'camomilla.MediaFolderTranslation'),
        ),
        migrations.AddField(
            model_name='sitemapurl',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.SitemapUrl', 'camomilla.SitemapUrlTranslation'),
        ),
        migrations.AddField(
            model_name='tag',
            name='_hvad_query',
            field=hvad.fields.SingleTranslationObject('camomilla.Tag', 'camomilla.TagTranslation'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Article'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Category'),
        ),
        migrations.AlterField(
            model_name='contenttranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Content'),
        ),
        migrations.AlterField(
            model_name='media',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='media_folder', to='camomilla.MediaFolder'),
        ),
        migrations.AlterField(
            model_name='mediafoldertranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.MediaFolder'),
        ),
        migrations.AlterField(
            model_name='mediatranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Media'),
        ),
        migrations.AlterField(
            model_name='sitemapurltranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.SitemapUrl'),
        ),
        migrations.AlterField(
            model_name='tagtranslation',
            name='master',
            field=hvad.fields.MasterKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Tag'),
        ),
    ]