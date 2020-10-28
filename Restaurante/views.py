from django.shortcuts import render, HttpResponse

def logIn(request):
    return HttpResponse("Pantalla de inicio de Sesion")


def home(request):
    return HttpResponse("Bienvenida Socio")



def altaProducto(request):
    return HttpResponse("Pantalla Alta Productos")


def inventario(request):
    return HttpResponse("Inventario")


def editarProducto(request):
    return HttpResponse("Editar productos")