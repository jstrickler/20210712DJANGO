"""
URL Configuration for chickens
"""
from django.urls import path
from . import views   # import views from app

app_name = "chickens"

urlpatterns = [
    # add url patterns for the chickens app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('', views.home, name='home'),
    path('cluck', views.cluck, name='cluck')
]
