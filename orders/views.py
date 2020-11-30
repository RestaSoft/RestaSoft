from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#vistas
def home_view_orders(request):
   
    return HttpResponse("Inicio de pagina ordenes")