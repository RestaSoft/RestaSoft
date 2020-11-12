# Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Products
from .forms import ProductsForm
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationFor
# Exception
from django.db.utils import IntegrityError
from django.contrib.auth.forms import UserCreationForm


# vistas


# def Productos(request):
#   products = Products.objects.all().order_by('-created')
#    return render(request,'products/products.html',{'products': products})

@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login.html')


def productos(request):
    # redirect to templates in templates/products
    prod = Products.objects.all()

    return render(request, 'products/products.html', {"prod": prod})


def buscar_prod(request):

    busqueda = request.GET["prd"]
    prod = Products.objects.filter(product_name__icontains=busqueda)

    return render(request, 'products/products.html', {"prod": prod, "query": busqueda})


@login_required
def nuevo_prod(request):

    if request.method == 'POST':
        product_name=request.POST['product_name']
        list_price=request.POST['list_price']
        category_name=request.POST['category_name']
        first_name=request.POST['first_name']
        image_prod=request.POST['image_prod']

        product = Products.objects.create(product_name=product_name,list_price=list_price, categoriesproduct=category_name, suppliers=first_name, image_prod=image_prod)
        product.product_name = request.POST['product_name']
        product.list_price = request.POST['list_price'] 
        product.categoriesproduct.category_name = request.POST['category_name']
        product.suppliers.first_name = request.POST['first_name']
        product.image_prod = request.POST ['image_prod']   
        product.save()

    return render(request, 'products/newproduct.html')



def delete_prod(request):

    if request.method == 'GET':
        delete = request.GET["delete"]
        borrar = Products.objects.get(id=delete)

        return render(request, 'products/delete.html', {"delete": borrar})

    if request.method == 'POST':
        delete = request.POST["delete"]
        borrar = Products.objects.get(id=delete)
        borrar.delete()
        return productos(request)
        # return render(request,'products/products.html')

    return render(request, 'products/delete.html')


def editar_prod(request):
    busqueda = request.GET["edit"]
    # redirect to templates in templates/products
    edit = Products.objects.filter(product_name__icontains=busqueda)
    producto_a_modificar = edit.first()

    return render(request, 'products/edit_products.html',
                  {"edit": edit, "query": busqueda, "prod_mod": producto_a_modificar})


def editar(request):

    return render(request, 'products/edit_products.html')
