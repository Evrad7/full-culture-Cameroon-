# Generated by Django 4.1.7 on 2023-04-07 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0028_content_position_alter_content_is_in_home_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['position'], 'verbose_name': 'contenu statique', 'verbose_name_plural': 'contenus statiques'},
        ),
    ]