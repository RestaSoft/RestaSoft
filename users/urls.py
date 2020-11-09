from django.urls import path, include
from users import views as users_views

urlpatterns = [
    
    # Users view
    path('',users_views.view_login, name="login"),
    path('newuser',users_views.newuser, name="newuser"),
    path('home/', users_views.home_view, name="home"),
    path('nosotros', users_views.nosotros_view, name="nosotros"),
    path('contacto', users_views.contacto_view, name="contacto"),
] 