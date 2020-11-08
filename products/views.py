#Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationFor


#vistas
def productos(request):
    #redirect to templates in templates/products
    return render (request, 'products/products.html')

def nuevo(request):
    return render (request, 'products/newproduct.html')

def edit_prod(request):
    #redirect to templates in templates/products
    return render (request, 'products/edit_prod.html')

