from django.urls import path, include
from users import views as user_views

urlpatterns = [
 # Django
    path('registrar', users_views.register, name="register"),
    path('',users_views.login, name="login"),
    path('alta',users_views.altausuario),

] 