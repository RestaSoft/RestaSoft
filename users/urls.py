from django.urls import path, include
<<<<<<< HEAD
from users import views as users_views


urlpatterns = [

    # Users views
    path('', users_views.login_view, name='login' ),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.register, name='signup'),
=======
from users import views as register_views

urlpatterns = [
 # Django
    path('registrar', register_views.register, name="register"),
    path('',register_views.registrar),
    path('alta',register_views.altausuario),
>>>>>>> 87583dfe8ab9d60c36cf9388039c5cdd948f5bd0

] 
