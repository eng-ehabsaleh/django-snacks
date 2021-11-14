from django.urls import path
from .views import Home, About, Snakes

urlpatterns = [
    path('', Snakes.as_view(), name='snake'),
    path('home', Home.as_view(), name='home'),
    path('about', About.as_view(), name='about')
]
