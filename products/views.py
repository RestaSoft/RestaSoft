#Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Products
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationFor


#vistas


#def Productos(request):
 #   products = Products.objects.all().order_by('-created')
#    return render(request,'products/products.html',{'products': products})

@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login.html')


def productos(request):
    #redirect to templates in templates/products
    prod = Products.objects.all()
    
    return render (request, 'products/products.html',{"prod":prod})

def buscar_prod(request):
    
    busqueda= request.GET["prd"]
    prod = Products.objects.filter(product_name__icontains=busqueda)

    return render(request,'products/products.html',{"prod":prod, "query":busqueda})
   # return HttpResponse(busqueda)

def nuevo(request):
    return render (request, 'products/newproduct.html')

def editar_prod(request):
    #redirect to templates in templates/products
    return render (request, 'products/edit_products.html')

