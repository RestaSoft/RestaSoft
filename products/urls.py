from django.urls import path, include
from products import views
urlpatterns = [
 # Django
    path('', views.home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)