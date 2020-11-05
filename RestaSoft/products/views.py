from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#vistas
def home(request):
   
    return HttpResponse("Inicio de pagina de productos")