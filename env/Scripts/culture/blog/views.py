from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
import operator
from django.views.generic import ListView, DetailView
from functools import reduce
from .models import Article
from .forms import CommentForm


class ArticlesView(ListView):
    paginate_by = 5
    model = Article
    context_object_name = "articles"
    template_name = "blog/articles.html"

    def get_queryset(self):
        sector = self.request.GET.get("sector")
        search = self.request.GET.get("search")
        query = []
        query.append(Q(published=True))
        if (sector != None) & (sector != "all"):
            query.append(Q(sector__slug=sector))
        if search != None:
            query.append(Q(title__icontains=search) |
                         Q(summary__icontains=search))
        query = reduce(operator.and_, query)
        queryset = super().get_queryset().filter(query)
        return queryset


class Articleview(DetailView):
    pk_url_kwarg = "slug"
    template_name = "blog/article.html"
    model = Article
    context_object_name = "article"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = super().get_queryset()
        object = get_object_or_404(
            queryset, sector__slug=self.kwargs["sector"], slug=self.kwargs["slug"])
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(
            sector__slug=self.kwargs["sector"]).exclude(slug=self.kwargs["slug"])[:5]
        if articles.count != 0:
            articles = Article.objects.exclude(slug=self.kwargs["slug"])[:2]
        context["articles"] = articles
        return context


def add_comment_ajax(request):
    errors = None
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save()
        comment = {"author": comment.author, "content": comment.content,
                   "created_at": comment.created_at.strftime("%d %B %Y %H:%M")}
        pass
    else:
        errors = form.errors
    return JsonResponse({"errors": errors, "comment": comment})


"""
def search_articles_ajax(request):
    sector = request.GET.get("sector")
    search = request.GET.get("search")
    query = []
    query.append(Q(published=True))
    if (sector != None) & (sector != "all"):
        query.append(Q(sector__slug=sector))
    if search != None:
        query.append(Q(title__icontains=search) |
                     Q(summary__icontains=search))
    query = reduce(operator.and_, query)
    articles = Article.objects.filter(query)
    articles = list(articles.values("slug", "image", "title", "summary"))

    return JsonResponse({"articles": articles})
"""
