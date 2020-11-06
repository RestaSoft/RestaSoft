from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



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

    
def login_view(request):
    ''' Login view '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request, 'users/login.html')



@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login')



@login_required
def home(request):
    return render(request, "RestaSoft/home.html")