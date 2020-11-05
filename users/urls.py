from django.urls import path, include
from users import views as register_views

urlpatterns = [
 # Django
    path('registrar', register_views.register, name="register"),
    path('',register_views.registrar),
    path('alta',register_views.altausuario),

] 
