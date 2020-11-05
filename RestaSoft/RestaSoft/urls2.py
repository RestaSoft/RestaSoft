from django.contrib import admin
from django.urls import path, include

# views
from django.contrib.auth import views as auth_views
from orders import views as orders_views
from users import views as users_views
from products import views as products_views

# static files config
 from django.conf import settings
 from django.conf.urls.static import static
    

urlpatterns = [
 # Django
    path('admin/', admin.site.urls),

 # orders views
    path('', orders_views.home_view, name='home'),
    path('new/',posts_views.create_post, name='create_post'),

# users views


# products views

#

# Restore password views
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
