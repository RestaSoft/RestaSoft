from django.urls import path, include
from django.shortcuts import render, redirect
from products import views as products_views

urlpatterns = [
 
    # path('', products_views.home, name="home"),

    # products view
    path('productos', products_views.productos, name="productos"),
    path('nuevo', products_views.nuevo, name="nuevo"),
    path('editar_prod',products_views.edit_prod, name="editar_prod"),

] 