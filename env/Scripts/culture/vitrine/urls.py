from django.urls import path
from .views import HomeView, SectorView, RegionView, ContactView, subscribe_newsletter_ajax

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sector/<slug:slug>", SectorView.as_view(), name="sector"),
    path("region/<slug:slug>", RegionView.as_view(), name="region"),
    path("contact", ContactView.as_view(), name="contact"),
    path("subscribe-newsletter/", subscribe_newsletter_ajax, name="newsletter")

]
