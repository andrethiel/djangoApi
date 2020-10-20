from django.urls import path

from . import views

urlpatterns = [
    path('', views.Robo, name='index'),
]