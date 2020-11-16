from django.urls import path, include
from django.shortcuts import render, redirect
from products import views as products_views

urlpatterns = [
 
    # path('', products_views.home, name="home"),

    # products view
    path('productos', products_views.productos, name="productos"),
    path('nuevo', products_views.nuevo, name="nuevo"),
    path('editar',products_views.editar, name="editar"),
    path('editar_prod',products_views.editar_prod, name="editar_prod"),
    path('buscar_prod',products_views.buscar_prod, name="buscar_prod"),
    path('delete_prod',products_views.delete_prod, name="delete_prod"),

] 