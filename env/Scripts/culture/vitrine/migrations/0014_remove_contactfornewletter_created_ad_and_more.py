# Generated by Django 4.1.7 on 2023-04-04 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0013_alter_contactfornewletter_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactfornewletter',
            name='created_ad',
        ),
        migrations.AddField(
            model_name='contactfornewletter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name="date d'ajout"),
            preserve_default=False,
        ),
    ]
