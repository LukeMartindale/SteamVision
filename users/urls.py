from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.base, name="base"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    # path('old-register/', views.Oldregister, name='old-register'),
    # path('old-login/', auth_views.LoginView.as_view(template_name="users/old_login.html"), name='old-login'),
    # path('old-login/', auth_views.LogoutView.as_view(), name='old-logout')
    # path('login/', views.loginPage, name='login')
]
