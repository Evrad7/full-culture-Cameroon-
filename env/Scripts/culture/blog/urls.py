
from django.urls import path
from .views import ArticlesView, Articleview

urlpatterns = [
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("<slug:sector>/<slug:slug>/", Articleview.as_view(), name="article"),
]
