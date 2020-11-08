from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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




=======
>>>>>>> be3cb568ae1ec9f4eb7125eafcfe7394587a5dab

def register(request):
    """ Register a new user """
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('WebApp:home')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

<<<<<<< HEAD
    
def login_view(request):
    ''' Login view '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('home.html')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request, 'users/login.html')



@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
=======
def logout(request):
    print("Hmmmmmmm")
>>>>>>> be3cb568ae1ec9f4eb7125eafcfe7394587a5dab
    return redirect('login')

def newuser(request):
    return render(request, 'users/signup.html')

def login(request):
    return render (request, 'users/login.html')

<<<<<<< HEAD

@login_required
def home(request):
    return render(request, "users/home.html")
=======
def altausuario(request):
    return HttpResponse('PRUEBA')
>>>>>>> be3cb568ae1ec9f4eb7125eafcfe7394587a5dab
