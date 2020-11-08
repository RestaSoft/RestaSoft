from django.urls import path, include
from users import views as users_views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
 # Django
    path('',user_views.login_view, name='login'),
    path('home/', user_views.home, name='home'),
=======
=======
>>>>>>> 4b3b705893dedbabf78e330d2abd2f160c28b619
    
    # Users view
    path('registrar', users_views.register, name="register"),
    path('',users_views.login, name="login"),
    path('alta',users_views.altausuario),
    path('newuser',users_views.newuser, name="newuser"),

<<<<<<< HEAD
>>>>>>> be3cb568ae1ec9f4eb7125eafcfe7394587a5dab
=======
=======
 # Django
    path('',user_views.login_view, name='login'),
    path('home/', user_views.home, name='home'),
>>>>>>> brendadev
>>>>>>> 4b3b705893dedbabf78e330d2abd2f160c28b619
] 