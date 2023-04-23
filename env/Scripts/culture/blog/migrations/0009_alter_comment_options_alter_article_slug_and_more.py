# Generated by Django 4.1.7 on 2023-04-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_tag_tag_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'commentaire', 'verbose_name_plural': 'commentaires'},
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, max_length=60),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(max_length=100, null=True, verbose_name='résumé'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60, verbose_name='titre'),
        ),
    ]
