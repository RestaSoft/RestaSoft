from django.urls import path, include
from users import views as users_views

urlpatterns = [
    
    # Users view
    path('registrar', users_views.register, name="register"),
    path('',users_views.login, name="login"),
    path('alta',users_views.altausuario),
    path('newuser',users_views.newuser, name="newuser"),

] 