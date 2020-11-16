from django.contrib import admin
from .models import Staffs
from .models import Products
from .models import Suppliers
from .models import CategoriesProduct
from .models import Stores
from .models import Permission
from .models import Stocks

# Register your models here.
class StaffsAdmin(admin.ModelAdmin): #Muesta las variables que deseemos que se vean en el modelo administrativo
    list_display=("phone",)
    search_fields=("phone",) #Campo de busqueda

admin.site.register(Staffs, StaffsAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display=("product_name", "list_price")
    search_fields=("product_name", "list_price")
    list_filter=("categoriesproduct",)

admin.site.register(Products, ProductsAdmin)

class SuppliersAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "email", "phone")
    search_fields=("first_name", "phone")

admin.site.register(Suppliers, SuppliersAdmin)

class CategoriesProductsAdmin(admin.ModelAdmin):
    list_display=("category_name", "category_description")


admin.site.register(CategoriesProduct, CategoriesProductsAdmin)

class StoresAdmin(admin.ModelAdmin):
    list_display=("store_name", "email", "phone")
    search_fields=("store_name", "phone")


admin.site.register(Stores, StoresAdmin)

admin.site.register(Permission)

admin.site.register(Stocks)