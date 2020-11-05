from django.urls import path, include
from django.shortcuts import render, redirect
from orders import views as orders_views


urlpatterns = [
 # Django
    path('', orders_views.home, name="home"),
] 