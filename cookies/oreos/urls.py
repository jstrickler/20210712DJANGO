"""
URL Configuration for oreos
"""
from django.urls import path
from . import views   # import views from app

app_name = "oreos"

urlpatterns = [
    path('', views.home, name="home"),
    path('dubl', views.dubl, name="dubl"),
    # add url patterns for the oreos app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
