from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def logout(request):
    print("Hmmmmmmm")
    return redirect('login')

def newuser(request):
    return render(request, 'users/signup.html')

def login(request):
    return render (request, 'users/login.html')

def altausuario(request):
    return HttpResponse('PRUEBA')