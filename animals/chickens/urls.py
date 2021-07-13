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
    path('cluck', views.cluck, name='cluck'),
    path('fail', views.fail, name='fail'),
    path('greet/<str:color>', views.greet, name='greet'),  # match anything but '/'
    path('repeat/<int:count>', views.repeat, name='repeat'),   # match 0-9+
    # path('mypath/<userid:id>', views.login, name='login'),  # custom converter
    path('<int:pk>', views.get_record, name='get_record')
]
