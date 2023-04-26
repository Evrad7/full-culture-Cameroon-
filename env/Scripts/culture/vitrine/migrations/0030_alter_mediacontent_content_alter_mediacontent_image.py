# Generated by Django 4.1.7 on 2023-04-07 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('vitrine', '0029_alter_content_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacontent',
            name='content',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vitrine.content', verbose_name='media_content'),
        ),
        migrations.AlterField(
            model_name='mediacontent',
            name='image',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='media_content'),
        ),
    ]