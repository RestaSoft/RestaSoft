from django.urls import path, include
from django.shortcuts import render, redirect
from products import views

urlpatterns = [
 # Django
    path('', views.home, name="home"),
] 