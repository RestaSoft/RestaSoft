from django.contrib import admin
from django.urls import path, include

# Static files config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
# Django
    path('admin/', admin.site.urls),
    
#urls de cada aplicacion
    path('',include('products.urls')),
    path('',include('users.urls')),
    path('orders/',include('orders.urls')),

] 