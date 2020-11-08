from django.urls import path, include
from django.shortcuts import render, redirect
from products import views as products_views

urlpatterns = [
 # Django
    path('', products_views.home, name="home"),
] 