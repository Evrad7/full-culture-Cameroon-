from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField
from filer.fields.image import FilerImageField
from vitrine.models import Sector


class Article(models.Model):
    slug = models.SlugField(max_length=60, editable=False, allow_unicode=False)
    banner = FilerImageField(
        null=True, on_delete=models.SET_NULL, verbose_name=_("image bannière"), related_name="article_banner")
    image = FilerImageField(
        null=True, on_delete=models.SET_NULL, verbose_name=_("image de présentation"), related_name="article_image")
    title = models.CharField(
        max_length=60, verbose_name=_("titre"), unique=True)
    summary = models.TextField(null=True, verbose_name=_("résumé"))
    published = models.BooleanField(
        default=False, blank=True, verbose_name=_("publié"))
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("date de création"))
    published_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("date de publication"))
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, verbose_name=_("date de la derniere modification"))
    content = QuillField(verbose_name=_("contenu de l'article"))
    sector = models.ForeignKey(
        to=Sector, null=True,  on_delete=models.SET_NULL, verbose_name=_("secteur"))

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog:article", kwargs={"sector": self.sector.slug, "slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title, allow_unicode=False)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        ordering = ["-created_at"]


class Comment(models.Model):
    author = models.CharField(max_length=60, verbose_name=_("auteur"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="date de création")
    content = models.CharField(max_length=250, verbose_name=_("message"))
    article = models.ForeignKey(
        to="Article", on_delete=models.CASCADE, verbose_name=_("article"))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("commentaire")
        verbose_name_plural = _("commentaires")


class Tag(models.Model):
    slug = models.SlugField(max_length=30, editable=False, allow_unicode=False)
    title = models.CharField(max_length=30, verbose_name=_("titre"))
    article = models.ForeignKey(
        to="Article", on_delete=models.CASCADE, verbose_name=_("article"))

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.title, allow_unicode=False)
        return super().save(*args, **kwargs)
