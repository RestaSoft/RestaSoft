from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Users view
    path('',users_views.view_login, name="login"),
    path('newuser',users_views.newuser, name="newuser"),
    path('home/', users_views.home_view, name="home"),
    path('logout', users_views.logout_view, name="logout"),
    path('nosotros', users_views.nosotros_view, name="about_us"),
    path('contacto', users_views.contacto_view, name="contact"),
    path('suscripcion', users_views.suscription_view, name="suscription"),

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
         name='password_reset_complete'),
] 