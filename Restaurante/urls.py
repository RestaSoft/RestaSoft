from django.contrib import admin
from django.urls import path
from Restaurante.views import logIn,home,altaProducto,editarProducto,inventario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logIn),
    path('home/', home),
    path('alta/', altaProducto),
    path('editar/', editarProducto),
    path('inventario/', inventario),
]
