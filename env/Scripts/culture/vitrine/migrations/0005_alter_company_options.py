# Generated by Django 4.1.7 on 2023-04-04 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0004_alter_company_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'default_permissions': ('change', 'view'), 'verbose_name': 'companie', 'verbose_name_plural': 'companie'},
        ),
    ]
