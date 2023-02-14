from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/', views.profilePage, name='profile'),
    path('profile/edit/', views.profileEditPage, name='profile-edit'),
]
