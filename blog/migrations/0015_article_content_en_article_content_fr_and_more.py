# Generated by Django 4.1.7 on 2023-04-23 10:05

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_article_options_alter_article_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=mdeditor.fields.MDTextField(null=True, verbose_name="contenu de l'article"),
        ),
        migrations.AddField(
            model_name='article',
            name='content_fr',
            field=mdeditor.fields.MDTextField(null=True, verbose_name="contenu de l'article"),
        ),
        migrations.AddField(
            model_name='article',
            name='summary_en',
            field=models.TextField(null=True, verbose_name='titre'),
        ),
        migrations.AddField(
            model_name='article',
            name='summary_fr',
            field=models.TextField(null=True, verbose_name='titre'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='titre'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_fr',
            field=models.CharField(max_length=60, null=True, verbose_name='titre'),
        ),
    ]