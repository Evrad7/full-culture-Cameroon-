from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from filer.fields.image import FilerImageField


class Sector(models.Model):
    slug = models.SlugField(max_length=60,  editable=False)
    name = models.CharField(max_length=60, unique=True, verbose_name="nom")
    description = models.TextField(
        max_length=150, null=True, blank=True, verbose_name=_("description"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.name, allow_unicode=False)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "secteur"
        verbose_name_plural = "secteurs"
        ordering = ["name"]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("vitrine:sector", kwargs={"slug": self.slug})


class Region(models.Model):
    slug = models.SlugField(max_length=30,  editable=False)
    name = models.CharField(max_length=30, unique=True, verbose_name=_("nom"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("description"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.name, allow_unicode=False)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("vitrine:region", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("région")
        verbose_name_plural = _("régions")
        ordering = ["name"]


class Company(models.Model):
    logo = FilerImageField(
        null=True, on_delete=models.SET_NULL, verbose_name=_("logo"))
    name = models.CharField(max_length=60, unique=True, verbose_name=_("name"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("description"))
    email = models.EmailField(unique=True, verbose_name=_("adresse email"))
    phone1 = models.CharField(max_length=16, validators=[RegexValidator(
        regex="^\+?[1-9]\d{1,14}$", message="numéro de téléphone incorrect")], unique=True, verbose_name=_("téléphone 1"))
    phone2 = models.CharField(max_length=16, validators=[RegexValidator(
        regex="^\+?[1-9]\d{1,14}$", message="numéro de téléphone incorrect")], null=True, unique=True, verbose_name=_("téléphone 2"))
    address = models.CharField(max_length=100, verbose_name=_("adresse"))
    slogan = models.CharField(max_length=30, null=True,
                              blank=True, verbose_name=_("slogan"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("companie")
        verbose_name_plural = _("companie")
        default_permissions = ("change", "view")


def default_company():
    try:
        return Company.objects.first()
    except:
        return None


class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name=_("nom"))
    email = models.EmailField(verbose_name=_("email"))
    subject = models.CharField(max_length=80, verbose_name=_("sujet"))
    description = models.TextField(
        max_length=400, verbose_name=_("description"))
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True, null=True, default=default_company
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")


class ContactForNewLetter(models.Model):
    email = models.EmailField(unique=True)
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True, null=True, default=default_company)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("date d'ajout"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("contact pour la newsletter")
        verbose_name_plural = _("contacts pour la newsletters")


class SocialLink(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=_("nom"))
    link = models.URLField(max_length=100, unique=True, verbose_name=_("lien"))
    icon_class = models.CharField(
        max_length=30, verbose_name=_("classe css de l'icon"))
    company = models.ForeignKey(
        to="Company", on_delete=models.CASCADE, blank=True, related_name="links")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("reseau social")
        verbose_name_plural = _("reseaux sociaux")
        ordering = ["pk"]


class Content(models.Model):
    title = models.CharField(max_length=80, verbose_name=_("titre"))
    body = models.TextField(verbose_name=_("corps"))
    sector = models.ForeignKey(
        to="Sector", null=True,  on_delete=models.SET_NULL, verbose_name=_("secteur"))
    region = models.ForeignKey(
        to="Region", null=True,  on_delete=models.SET_NULL, verbose_name=_("region"))
    is_in_home_page = models.BooleanField(
        default=False, verbose_name=_("Affiché à la page d'accueil"))
    position = models.PositiveSmallIntegerField(default=100, blank=True, verbose_name=_("position d'affichage dans le site"),
                                                help_text=_("Plus ce nombre est petit plus le contenu s'affichera en haut avant les autres"))
    pattern_content_home_page = models.ForeignKey(
        to="PatternContent", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("modèle d'affichage dans la page d'accueil"), help_text=_("modèle d'affichage du contenu dans la page d'accueil"), related_name="content_home_page")
    pattern_content_others_pages = models.ForeignKey(
        to="PatternContent", null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("modèle d'affichage dans d'autres pages"), help_text=_("modèle d'affichage du contenu dans des pages autres que la page d'accueil"), related_name="content_others_pages")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("vitrine:sector", kwargs={"slug": self.sector.slug})

    class Meta:
        verbose_name = _("contenu statique")
        verbose_name_plural = _("contenus statiques")
        ordering = ["position"]


class PatternContent(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    title = models.CharField(max_length=80, verbose_name=_("nom"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("modele d'affichage des contenus statiques")
        verbose_name_plural = _("modeles d'affichage des contenus statiques")


class MediaContent(models.Model):
    content = models.ForeignKey(
        to="Content", on_delete=models.CASCADE, blank=True, verbose_name=_("contenu"))
    image = FilerImageField(
        null=True, on_delete=models.SET_NULL, verbose_name=_("image"))

    class Meta:
        verbose_name = _("media du contenu")
        verbose_name_plural = _("medias du contenu")
        ordering = ["pk"]
