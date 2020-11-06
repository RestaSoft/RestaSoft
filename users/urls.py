from django.urls import path, include
from users import views as users_views

urlpatterns = [
 # Django
    path('registrar', users_views.register, name="register"),
    path('',users_views.registrar, name="login"),
    path('alta',users_views.altausuario),

] 