''' Users Views. '''
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from django.db import models
from users.models import Staffs
from users.models import Stores
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.utils import IntegrityError
from cloudinary.forms import cl_init_js_callbacks

# Forms
from users.forms import StaffsForm
from .forms import StoresForm, UserForm
from .forms import PictureForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('/')


def newuser(request):
    """ Sign up view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password do not match'})

        try:
            # from users.models import Staffs
            user = User.objects.create_user(username=username, password=password)

        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        staff = Staffs(user=user)
        staff.phone = request.POST['phone']
        staff.save()
        store = Stores(user=user)
        store.city = request.POST ['city']
        store.address = request.POST['address']
        store.store_name = request.POST['store_name']
        store.zip_code = request.POST ['zip']
        store.slogan = request.POST['slogan']
        store.sitio_web = request.POST ['sitio_web']
        #store.image = request.POST ['image']
        if request.method == 'POST' and request.FILES['image']:
            store.image = request.FILES['image']
        store.save()

        return redirect('login')

    return render(request, 'users/signup.html')




def view_login(request):
    ''' Login view '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('home')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request, 'users/login.html')



@login_required
def home_view(request):
        return render(request, 'home.html')


def nosotros_view(request):
    return render(request, 'company/about_us.html')


def contacto_view(request):

    if request.method == 'POST':
        asun = request.POST ['asunto']
        mensaj = request.POST ['mensaje'] + " " + request.POST ['correo'] + ", " + request.POST ['nombre'] + " " + request.POST ['apellido'] + ", " + request.POST['telefono']

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["restasoftapp@gmail.com"]
        send_mail(asun, mensaj, email_from, recipient_list)
        return render(request, 'company/gracias.html')
    return render(request, 'company/contact.html')


def suscription_view(request):
    return render(request, 'company/suscription.html')




