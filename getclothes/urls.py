from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('list', views.list, name="list"),
    path('list_db', views.list_db, name="list_db"),
    path('recommend', views.recommend, name="recommend"),
    path('re_home', views.re_home, name="re_home"),
    path('list_edit', views.list_edit, name="list_edit"),
    path('update', views.update, name="update")
]