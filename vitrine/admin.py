from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Sector, Region, Company, SocialLink, Contact, ContactForNewLetter, Content, MediaContent,\
    PatternContent


@admin.register(Sector)
class SectorAdmin(TabbedTranslationAdmin):
    fields = ["name", "description"]
    list_display = ["slug", "name", "description"]
    search_fields = ["name", "description"]
    # prepopulated_fields = {"slug": ("name",)}


@admin.register(Region)
class RegionAdmin(TabbedTranslationAdmin):
    fields = ["name", "description"]
    list_display = ["slug", "name", "description"]
    search_fields = ["name", "description"]


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    fields = ["name", "link", ]
    extra = 1
    max_num = 5
    verbose_name = "réseau social de la companie"
    verbose_name_plural = "réseaux sociaux de la companie"


@admin.register(Company)
class CompanyAdmin(TabbedTranslationAdmin):
    fields = ["logo", "name", "slogan", "description",
              "email", "phone1", "phone2", "address"]
    list_display = ["name", "slogan", "logo", "email", "phone1"]
    inlines = [SocialLinkInline]

    def has_add_permission(self, request) -> bool:
        return True

    def has_delete_permission(self, request, obj=None) -> bool:
        return True


@admin.register(Contact)
class ContactAdmimn(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "description"]
    search_fields = ["name", "email", "subject", "description"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(ContactForNewLetter)
class ContactForNewLetterAdmimn(admin.ModelAdmin):
    fields = ["email"]
    list_display = ["email", "created_at"]
    search_fields = ["email"]


class MediaContentInline(admin.TabularInline):
    model = MediaContent
    fields = ["image"]
    pk_name = "content"
    extra = 1
    verbose_name = "image"
    verbose_name_plural = "images"
    max_num = 20


@admin.register(Content)
class ContentAdmin(TabbedTranslationAdmin):
    fields = ["region", "sector", "title", "body",
              "is_in_home_page", "position", "pattern_content_home_page", "pattern_content_others_pages"]
    list_display = ["title", "region", "sector", "position"]
    search_fields = ["title", "sector__name", "region__name"]
    list_filter = ["region", "sector"]
    inlines = [MediaContentInline]


@admin.register(PatternContent)
class PatternContentAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
