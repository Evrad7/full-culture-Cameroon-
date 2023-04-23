# Generated by Django 4.1.7 on 2023-04-04 10:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vitrine.models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0012_alter_company_description_alter_company_slogan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactfornewletter',
            options={'verbose_name': 'contact pour la newsletter', 'verbose_name_plural': 'contacts pour la newsletters'},
        ),
        migrations.AddField(
            model_name='contactfornewletter',
            name='created_ad',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(blank=True, default=vitrine.models.default_company, null=True, on_delete=django.db.models.deletion.CASCADE, to='vitrine.company'),
        ),
        migrations.AlterField(
            model_name='contactfornewletter',
            name='company',
            field=models.ForeignKey(blank=True, default=vitrine.models.default_company, null=True, on_delete=django.db.models.deletion.CASCADE, to='vitrine.company'),
        ),
    ]
