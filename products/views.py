#Imports
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


#vistas


#def Productos(request):
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
    prod = Products.objects.all()
    
    return render (request, 'products/products.html',{"prod":prod})

def buscar_prod(request):
    
    busqueda= request.GET["prd"]
    prod = Products.objects.filter(product_name__icontains=busqueda)

    return render(request,'products/products.html',{"prod":prod, "query":busqueda})


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
    

    if request.method=='GET':
        delete= request.GET["delete"]
        borrar = Products.objects.get(id = delete )

        return render(request,'products/delete.html',{"delete":borrar})


    if request.method== 'POST':
        delete= request.POST["delete"]
        borrar = Products.objects.get(id = delete )
        borrar.delete()
        return productos(request)
        #return render(request,'products/products.html')
    
    return render(request,'products/delete.html')







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
         #redirect to templates in templates/products
        edit = Products.objects.filter(product_name__icontains=busqueda)
        producto_a_modificar=edit.first()
    
        return render (request, 'products/edit_products.html',{"edit":edit,"query":busqueda,"prod_mod":producto_a_modificar})
    if request.method == 'POST':
        id_pro= request.POST["save"]
        nombre= request.POST["name"]
        modify =Products.objects.get(id=id_pro)


        modify.product_name=nombre
        modify.save()
        return productos(request)

        print(modify)
        #producto_a_modificar.product_name = editar

        
        # producto_a_modificar.product_name = editar.product_name
        # producto_a_modificar.categoriesproduct=editar.categoriesproduct
        # producto_a_modificar.list_price=editar.list_price
        # producto_a_modificar.suppliers=editar.suppliers
        # producto_a_modificar.image_prod=producto_a_modificar.image_prod

    return render(request, 'products/edit_products.html')
    
        



def editar(request):
    
    return render (request, 'products/edit_products.html')
#     form = ProductsForm()
#     if request.method == 'POST':
#         #print(request.POST)
#         form = ProductsForm(request.POST, request.FILES)

#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect("productos")
#             except IntegrityError:
                
#                 return render(request, 'products/newproduct.html', {'error': 'Producto en existencia'})
#     context = {'form':form}

     

