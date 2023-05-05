from django.urls import path
from .views import HomeView, SectorView, RegionView, get_contact_view, post_contact_view, subscribe_newsletter_ajax

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sector/<slug:slug>", SectorView.as_view(), name="sector"),
    path("region/<slug:slug>", RegionView.as_view(), name="region"),
    path("contact", get_contact_view, name="contact"),
    path("contact-post/", post_contact_view, name="contact_post"),
    path("subscribe-newsletter/", subscribe_newsletter_ajax, name="newsletter"),

]
