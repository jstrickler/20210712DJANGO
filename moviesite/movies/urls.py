"""
URL Configuration for movies
"""
from django.urls import path
from . import views   # import views from app

app_name = "movies"

urlpatterns = [
    # add url patterns for the movies app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('', views.home, name='home'),
    path('list', views.movie_list, name='movie_list'),
    path('details/<str:pk>', views.movie_details, name='movie_details'),
    path('form', views.movie_form, name='movie_form'),
]
