"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views

<<<<<<< HEAD
app_name = "superheroes"
=======
app_name = 'superheroes'
>>>>>>> 31ee024df05c1bbba52ee7853427671b3002c6ae

urlpatterns = [
    path('', views.home, name='home'),
    path('demoform', views.demoform, name='demoform'),
    path('heroform', views.heroform, name='heroform'),
    path('heroadd', views.heroadd, name='heroadd'),
    path('herolist', views.herolist, name='herolist'),
]

