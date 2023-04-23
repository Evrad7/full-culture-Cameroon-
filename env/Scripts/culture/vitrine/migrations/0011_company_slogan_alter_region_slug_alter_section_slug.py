# Generated by Django 4.1.7 on 2023-04-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0010_alter_region_slug_alter_section_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slogan',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, max_length=60),
        ),
    ]
