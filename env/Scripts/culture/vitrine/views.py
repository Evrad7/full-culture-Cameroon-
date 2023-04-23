from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Sector, Region, Content, ContactForNewLetter
from .forms import ContactForm, NewLetterForm
from blog.models import Article


class HomeView(TemplateView):
    template_name = "vitrine/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contents"] = Content.objects.filter(is_in_home_page=True)
        context["articles"] = Article.objects.all()[:4]

        return context


class SectorView(DetailView):
    model = Sector
    template_name = "vitrine/sector.html"
    slug_url_kwarg = "slug"
    context_object_name = "sector"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class RegionView(DetailView):
    model = Region
    template_name = "vitrine/region.html"
    slug_url_kwarg = "slug"
    context_object_name = "region"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class ContactView(CreateView):
    form_class = ContactForm
    template_name = "vitrine/contact.html"

    def get_success_url(self):
        from django.urls import reverse
        success_url = reverse("vitrine:home")
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


def subscribe_newsletter_ajax(request):
    print(request.method)
    if request.method == "POST":
        form = NewLetterForm(request.POST)
        print("--------------------------------------")
        print(request.POST)
        print("-----------------------")
        if form.is_valid():
            email = form.cleaned_data["email"]
            ContactForNewLetter.objects.get_or_create(email=email)
            errors = None
        else:
            errors = form.errors

        return JsonResponse({"errors": errors})
