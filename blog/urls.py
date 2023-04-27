
from django.urls import path
from .views import ArticlesView, Articleview, add_comment_ajax

urlpatterns = [
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("<slug:sector>/<slug:slug>/", Articleview.as_view(), name="article"),
    path("add-comment-ajax/", add_comment_ajax, name="add_comment"),
]
