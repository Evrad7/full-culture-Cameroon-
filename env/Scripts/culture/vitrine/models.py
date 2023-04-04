from django.db import models
from django.core.validators import RegexValidator
from filer.fields.image import FilerImageField


class Section(models.Model):
    slug = models.SlugField(max_length=60)
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    content = models.ForeignKey(
        to="Content", null=True,  on_delete=models.SET_NULL)


class Region(models.Model):
    slug = models.SlugField(max_length=30)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=150, null=True, blank=True)


class Company(models.Model):
    logo = FilerImageField(null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=100)
    email = models.EmailField(unique=True)
    phone1 = models.CharField(max_length=16, validators=[RegexValidator(
        regex="^\+?[1-9]\d{1,14}$", message="numéro de téléphone incorrect")], unique=True)
    phone2 = models.CharField(max_length=16, validators=[RegexValidator(
        regex="^\+?[1-9]\d{1,14}$", message="numéro de téléphone incorrect")], null=True, unique=True)
    address = models.TextField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    description = models.TextField(max_length=400)
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True)


class ContactForNewLetter(models.Model):
    email = models.EmailField()
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True)


class SocialLink(models.Model):
    name = models.CharField(max_length=30, unique=True)
    link = models.URLField(max_length=100, unique=True)
    incon_class = models.CharField(max_length=30)
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True)


class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)


class MediaContent(models.Model):
    content = models.ForeignKey(
        to="Content", on_delete=models.CASCADE, blank=True)
    image = FilerImageField(null=True, on_delete=models.SET_NULL)
