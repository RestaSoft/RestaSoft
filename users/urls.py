from django.urls import path, include
from users import views as users_views

urlpatterns = [
<<<<<<< HEAD
 # Django
    path('',user_views.login_view, name='login'),
    path('home/', user_views.home, name='home'),
=======
    
    # Users view
    path('registrar', users_views.register, name="register"),
    path('',users_views.login, name="login"),
    path('alta',users_views.altausuario),

>>>>>>> be3cb568ae1ec9f4eb7125eafcfe7394587a5dab
] 