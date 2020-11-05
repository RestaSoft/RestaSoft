from django.urls import path, include
from users import views

urlpatterns = [
 # Django
    path('registrar', views.register, name="register"),
    path('',views.registrar),

] 
