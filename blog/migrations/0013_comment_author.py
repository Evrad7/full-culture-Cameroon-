# Generated by Django 4.1.7 on 2023-04-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='anonyme', max_length=60),
            preserve_default=False,
        ),
    ]
