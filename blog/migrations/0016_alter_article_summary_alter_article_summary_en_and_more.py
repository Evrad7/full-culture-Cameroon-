# Generated by Django 4.1.7 on 2023-04-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_article_content_en_article_content_fr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, verbose_name='résumé'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary_en',
            field=models.TextField(null=True, verbose_name='résumé'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary_fr',
            field=models.TextField(null=True, verbose_name='résumé'),
        ),
    ]