# Generated by Django 4.1.7 on 2023-04-04 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_section_article_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
            preserve_default=False,
        ),
    ]
