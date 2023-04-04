from django.db import models
from mdeditor.fields import MDTextField
from filer.fields.image import FilerImageField
from vitrine.models import Section


class Article(models.Model):
    slug = models.SlugField(max_length=30)
    banner = FilerImageField(null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    summary = models.TextField(max_length=10, null=True)
    published = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    content = MDTextField()
    section = models.ForeignKey(
        to=Section, null=True,  on_delete=models.SET_NULL)
    tag = models.ManyToManyField(to="Tag")


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=250)
    article = models.ForeignKey(to="Article", on_delete=models.CASCADE)


class Tag(models.Model):
    slug = models.SlugField(max_length=30)
    title = models.CharField(max_length=30)
