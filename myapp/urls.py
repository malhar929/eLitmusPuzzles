from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),

    path("login", views.loginpage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerpage, name="register"),

    path("puzzle1", views.puzzle1, name="puzzle1"),
    path("puzzle2", views.puzzle2, name="puzzle2"),
    path("puzzle3", views.puzzle3, name="puzzle3"),
]
