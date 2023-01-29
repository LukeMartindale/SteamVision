from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .decorators import unauthrosied_user

# Create your views here.

def base(request):
    return render(request, 'users/base.html')

@unauthrosied_user
def registerPage(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/register.html', context)

#Login Page and Functionality
@unauthrosied_user
def loginPage(request):
    if request.method == 'POST':
        
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
        
    return render(request, 'users/login.html')

#Logout Functionality
def logoutPage(request):
    logout(request)
    return redirect('login')

def Oldregister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created!")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/old_register.html', {'form': form})


