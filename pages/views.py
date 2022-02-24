from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView (TemplateView):
    template_name = "pages_templates/home.html"

class AboutPageView (TemplateView):
    template_name = "pages_templates/about.html"
# Create your views here.
