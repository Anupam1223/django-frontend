from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "travel"
urlpatterns = [
    path("", views.AboutView.as_view(template_name="index.html"), name="aboutview"),
]
