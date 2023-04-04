from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Article


class ArticlesView(ListView):
    paginate_by = 5
    model = Article
    context_object_name = "articles"
    template_name = "blog/articles.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class Articleview(DetailView):
    pk_url_kwarg = "slug"
    template_name = "blog/article.html"
    model = Article
    context_object_name = "article"

    def get_object(self, queryset=None):
        object = None
        # object=super().get_object(queryset)
        return object
