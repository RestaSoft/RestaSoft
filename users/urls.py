from django.urls import path, include
from users import views as users_views


urlpatterns = [

    # Users views
    path('', users_views.login_view, name='login' ),
    path('logout/', users_views.logout_view, name='logout'),
    path('signup/', users_views.register, name='signup'),

] 
