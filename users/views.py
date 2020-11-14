''' Users Views. '''
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from django.db import models
from users.models import Staffs
from users.models import Stores
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#Forms
from users.forms import StaffsForm




@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login.html')




def newuser(request):
    """ Sign up view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password do not match'})

        try:
            #from users.models import Staffs
            user = User.objects.create_user(username=username, password=password)
         
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        staff=Staffs(user=user)
        staff.save()

        return redirect('login')

    return render(request,'users/signup.html')



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

    return render (request, 'users/login.html')


@login_required
def home_view(request):
     return render (request, 'home.html')


def nosotros_view(request):
    return render(request, 'nosotros.html')

def contacto_view(request):    
    return render(request, 'contacto.html')

def suscription_view(request):    
    return render(request, 'company/suscription.html')