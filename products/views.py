# Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Products, Stores, Staffs, CategoriesProduct
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
    # redirect to templates in templates/products

    usuario = request.user
    nombre = usuario.staffs.stores.store_name

    if nombre != "Admin":
        usuario = usuario.staffs.stores.id
        prod = Products.objects.filter(stores_id=usuario)
        return render(request, 'products/products.html', {"prod": prod})

    prod = Products.objects.all()
    return render(request, 'products/products.html', {"prod": prod})


@login_required
def buscar_prod(request):

    usuario = request.user
    nombre = usuario.staffs.stores.store_name
    usuario = usuario.staffs.stores.id
    busqueda = request.GET["prd"]

    if nombre != "Admin":
        prod = Products.objects.filter(
            product_name__icontains=busqueda).filter(stores_id=usuario)
        return render(request, 'products/products.html', {"prod": prod, "query": busqueda})

    prod = Products.objects.filter(product_name__icontains=busqueda)
    return render(request, 'products/products.html', {"prod": prod, "query": busqueda})


@login_required
def nuevo(request):
    if request.method == 'POST':
        precio= request.POST["price"]
        nomb= request.POST["name"]
        cat_nom= request.POST["categoria"]
        desc= request.POST['description']
        stor_name = request.POST['select']
        #creacion de objetos
        usuario= request.user
        nombre = usuario.staffs.stores.store_name
        if nombre != "Admin":

            cat = CategoriesProduct.objects.create(category_name=cat_nom, category_description=desc)
            tienda = Stores.objects.get(store_name=nombre)
            modify =Products.objects.create(product_name=nomb, list_price=precio, categoriesproduct=cat, stores=tienda)
        if nombre == "Admin":
        
            return HttpResponse("Usuario "+ nombre +" no puede añadir productos")
        

        if request.method == 'POST' and request.FILES['image']:
            modify.image_prod = request.FILES['image']
        modify.save()
        return productos(request)
        
    return render(request, 'products/newproduct.html')
    

@login_required
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



@login_required
def comandas(request):
    
    return render (request, 'products/commands.html')


@login_required
def editar_prod(request):
    
    if request.method=='GET':
        busqueda= request.GET["edit"]
        usuario= request.user
        nombre = usuario.staffs.stores.store_name
        usuario=usuario.staffs.stores.id
         # redirect to templates in templates/products
        if nombre != "Admin":
            edit = Products.objects.filter(product_name__icontains=busqueda).filter(stores_id=usuario)
            producto_a_modificar=edit.first()
            return render (request, 'products/edit_products.html',{"edit":edit,"query":busqueda,"prod_mod":producto_a_modificar})
        edit = Products.objects.filter(product_name__icontains=busqueda)
        producto_a_modificar=edit.first()
        return render (request, 'products/edit_products.html',{"edit":edit,"query":busqueda,"prod_mod":producto_a_modificar})
    if request.method == 'POST':
        # SE ASIGNAN NUEVOS VALORES
        precio= request.POST["price"]
        nombre= request.POST["name"]
        id_pro= request.POST["save"]
        descri= request.POST["description"]
        nomb= request.POST["catname"]
        print(nomb)
        cat = CategoriesProduct.objects.filter(category_name=nomb)
        cat = cat.first()
        cat.category_description=descri
        modify =Products.objects.get(id=id_pro)
        modify.list_price=precio
        modify.product_name=nombre
        # SI CONTIENE IMAGEN SE MODIFICARA.
        if request.FILES:
            imagen=request.FILES["img"]
            modify.image_prod=imagen
        # SE GUARDA EL ARTICULO
        cat.save()
        modify.save()
        
        return productos(request)

    return render(request, 'products/edit_products.html')
    
        


@login_required
def editar(request):
    
    return render (request, 'products/edit_products.html')
