# Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Products,Stores,Staffs
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


@login_required
def productos(request):
    #redirect to templates in templates/products

    usuario= request.user
    usuario=usuario.stores.id
    if usuario:
        print(usuario)
        prod = Products.objects.filter(stores_id=usuario)
        return render (request, 'products/products.html',{"prod":prod})
    prod = Products.objects.all()
    return render (request, 'products/products.html',{"prod":prod})
    
    

def buscar_prod(request):
    
    usuario= request.user
    usuario=usuario.staffs.stores.id
    print(usuario)
    busqueda= request.GET["prd"]
    prod = Products.objects.filter(product_name__icontains=busqueda).filter(stores_id=usuario)

    return render(request, 'products/products.html', {"prod": prod, "query": busqueda})


def nuevo(request):
    form = ProductsForm()
    if request.method == 'POST':
        #print(request.POST)
        form = ProductsForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                return redirect("productos")
            except IntegrityError:
                
                return render(request, 'products/newproduct.html', {'error': 'Username already taken'})


    context = {'form':form}
    print

    return render (request, 'products/newproduct.html', context)


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






#POR SI LAS DUDAS

# def editar_prod(request):
#     form = ProductsForm()
#     if request.method == 'POST':
#         #print(request.POST)
#         form = ProductsForm(request.POST, request.FILES)

#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect("productos")
#             except IntegrityError:
                
#                 return render(request, 'products/edit_products.html', {'error': 'Ya hay articulos iguales'})


#     context = {'form':form}

#     return render (request, 'products/edit_products.html', context)



def editar_prod(request):
    
    if request.method=='GET':
        busqueda= request.GET["edit"]
        usuario= request.user
        usuario=usuario.staffs.stores.id
         #redirect to templates in templates/products
        edit = Products.objects.filter(product_name__icontains=busqueda).filter(stores_id=usuario)
        producto_a_modificar=edit.first()
    
        return render (request, 'products/edit_products.html',{"edit":edit,"query":busqueda,"prod_mod":producto_a_modificar})
    if request.method == 'POST':
        #SE ASIGNAN NUEVOS VALORES
        description= request.POST["description"]
        precio= request.POST["price"]
        nombre= request.POST["name"]
        id_pro= request.POST["save"]
        modify =Products.objects.get(id=id_pro)
        modify.list_price=precio
        modify.product_name=nombre
        #SI CONTIENE IMAGEN SE MODIFICARA.
        if request.FILES:
            imagen=request.FILES["img"]
            modify.image_prod=imagen
        #SE GUARDA EL ARTICULO
        modify.save()
        return productos(request)

    return render(request, 'products/edit_products.html')
    
        



def editar(request):
    
    return render (request, 'products/edit_products.html')

     

