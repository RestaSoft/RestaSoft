from django.urls import path, include
from users import views as user_views

urlpatterns = [
 # Django
    path('',user_views.login_view),
    path('home/', user_views.home),
] 