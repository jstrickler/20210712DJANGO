"""
URL Configuration for apiv1
"""
from django.urls import path
from . import views   # import views from app

app_name = 'apiv1'

urlpatterns = [
    # add url patterns for the apiv1 app here

    # Example:
    path('herolist', views.superhero_list, name='superherolist'),
    path('hero/<int:pk>', views.superhero_detail, name='superherodetail'),
    path('enemylist', views.EnemyList.as_view(), name='enemylist'),
    path('enemy/<int:pk>', views.EnemyDetail.as_view(), name='enemydetail'),
]
