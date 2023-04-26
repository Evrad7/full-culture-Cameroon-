from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, DetailView, CreateView
from throttle.decorators import throttle
from django.utils.decorators import method_decorator
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


def get_contact_view(request):
    form = ContactForm()
    return render(request, "vitrine/contact.html", {"form": form})


@throttle(zone="contact")
def post_contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("vitrine:home"))
    else:
        return redirect(reverse("vitrine:contact"))


def subscribe_newsletter_ajax(request):
    errors = None
    message = None
    if request.method == "POST":
        form = NewLetterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            ContactForNewLetter.objects.get_or_create(email=email)
            message = _("Ajout à la newsletter réussi")
        else:
            errors = form.errors

        return JsonResponse({"errors": errors, "message": message})
