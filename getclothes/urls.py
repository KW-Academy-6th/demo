from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('list', views.list, name="list")
]