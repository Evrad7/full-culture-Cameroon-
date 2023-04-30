# Generated by Django 4.1.7 on 2023-04-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_article_content_alter_article_content_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=60, null=True, unique=True, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fr',
            field=models.CharField(max_length=60, null=True, unique=True, verbose_name='titre'),
        ),
    ]
