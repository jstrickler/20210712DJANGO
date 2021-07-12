from django.urls import path
from . import views  # import views module from current folder

app_name = 'oatmeal'  #  specify APP name (not project)

urlpatterns = [
    path('', views.hello, name='hello'),
    path('cheese/', views.cheese, name='cheese'),
]
