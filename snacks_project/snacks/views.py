from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Snakes(TemplateView):
    template_name = 'base.html'


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'
