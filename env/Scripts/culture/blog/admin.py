from django.contrib import admin
from .models import Comment, Article, Tag
from .forms import CommentAdminForm


class TagAdmin(admin.TabularInline):
    model = Tag
    fileds = ["title"]
    extra = 0
    max_num = 2


class CommentInline(admin.TabularInline):
    form = CommentAdminForm
    model = Comment
    fields = ["content"]
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["sector", "banner", "image", "title",  "summary",
              "published", "content"]
    list_display = ["title", "summary", "published"]
    list_filter = ["title", "published", "sector"]
    ordering = ["title"]
    search_fields = ["title", "summary", "sectpr__name"]
    inlines = [TagAdmin, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "created_at", "content"]
    search_fields = ["content", "article__name"]
    list_filter = ["article"]
    ordering = ["-created_at"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ["title", "article"]
    list_display = ["slug", "title", "article"]
    search_fields = ["title"]
    list_filter = ["article"]
