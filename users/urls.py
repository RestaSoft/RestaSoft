from django.urls import path, include
from users import views as users_views

urlpatterns = [
<<<<<<< HEAD
    
    # Users view
    path('registrar', users_views.register, name="register"),
    path('',users_views.login, name="login"),
    path('alta',users_views.altausuario),
    path('newuser',users_views.newuser, name="newuser"),

=======
 # Django
    path('',user_views.login_view, name='login'),
    path('home/', user_views.home, name='home'),
>>>>>>> brendadev
] 