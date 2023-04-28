from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .decorators import unauthrosied_user

from django.contrib.auth.models import User
from home.models import Game
from users.models import Profile

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
            user = User.objects.get(username=request.POST["username"])
            profile = Profile()
            profile.user = user
            profile.save()

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
    profile = Profile.objects.get(user=user)

    print(profile.followed_games)

    if profile.followed_games != [] or {} or [{}]:
        game_ids = [i["app_id"] for i in profile.followed_games]
    else:
        game_ids = []

    print(game_ids)
    # Get game objects
    followed_games = Game.objects.filter(app_id__in=game_ids).order_by('name')

    context = {'user': user, 'profile': profile, 'followed_games': followed_games}

    return render(request, 'users/profile.html', context)

#Profile edit Page
@login_required
def profileEditPage(request):
    form = UserUpdateForm()

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, 'Account info successfully updated')
            print("TEST")

    user = User.objects.get(username=request.user)

    context = {'form': form}

    return render(request, 'users/profile-edit.html', context)

# Profile update password Page
@login_required
def profileEditPasswordPage(request):
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, 'Account password successfully updated')


        else:
            print(request.POST)
            print(request.POST['old_password'])
            print(request.POST['new_password1'])
            print(request.POST['new_password2'])

    context = {'form': form}
    return render(request, 'users/profile-edit-password.html', context)
