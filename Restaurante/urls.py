from django.contrib import admin
from django.urls import path, include
# from . import views
# from Restaurante.views import logIn,home,altaProducto,editarProducto,inventario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('WebApp.urls'))
]
