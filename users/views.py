from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthrosied_user

from django.contrib.auth.models import User

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

#Profile Page
@login_required
def profilePage(request):
    user = User.objects.get(username=request.user)

    context = {'user': user}

    return render(request, 'users/profile.html', context)

#Profile edit Page
@login_required
def profileEditPage(request):

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            print("TEST")

    user = User.objects.get(username=request.user)

    context = {'user': user}

    return render(request, 'users/profile-edit.html')
