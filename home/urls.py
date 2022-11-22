from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.games, name='game'),
    path('test/', views.test, name='test')
]
