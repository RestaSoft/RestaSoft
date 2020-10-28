from django.shortcuts import render, HttpResponse

def logIn(request):
    return render(request, "Restaurante/login.html")


def home(request):
    return  render(request, "Restaurante/home.html")



def altaProducto(request):
    return  render(request, "Restaurante/alta.html")



def inventario(request):
    return  render(request, "Restaurante/inventario.html")



def editarProducto(request):
    return  render(request, "Restaurante/editar.html")
