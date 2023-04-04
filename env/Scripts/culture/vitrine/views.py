from django.shortcuts import render, HttpResponseRedirect


from django.views.generic import TemplateView, DetailView, CreateView
from .models import Section, Region, Contact
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "vitrine/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SectorView(DetailView):
    model = Section
    template_name = "vitrine/sector.html"
    slug_url_kwarg = "slug"
    context_object_name = "sector"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        return None
        # return super().get_object(queryset)


class RegionView(DetailView):
    model = Region
    template_name = "vitrine/region.html"
    slug_url_kwarg = "slug"
    context_object_name = "region"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        return None
        # return super().get_object(queryset)


class ContactView(CreateView):
    form_class = ContactForm
    template_name = "vitrine/contact.html"

    def get_success_url(self):
        from django.urls import reverse
        success_url = reverse("vitrine:contact")
        return success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())
        # return super().form_valid(form)
