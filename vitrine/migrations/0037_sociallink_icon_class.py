# Generated by Django 4.1.7 on 2023-04-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0036_remove_sociallink_icon_class_alter_sociallink_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='icon_class',
            field=models.CharField(default='', max_length=30, verbose_name="classe css de l'icon"),
            preserve_default=False,
        ),
    ]
