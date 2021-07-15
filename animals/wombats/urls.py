"""
URL Configuration for wombats
"""
from django.urls import path
from . import views   # import views from app

app_name = "wombats"

urlpatterns = [
#    'api/wombat/<uuid:pk>', views.wombat_get, 'wombat',
    # add url patterns for the wombats app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
