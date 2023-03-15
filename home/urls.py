from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.GameList, name='game-list'),
    path('games/<int:pk>/', views.GameDetail, name='game-detail'),
    path('games/<int:pk>/reviews/', views.GameReviews, name='game-reviews'),
]
