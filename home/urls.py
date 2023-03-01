from django.urls import path
from . import views
from . views import (
    OldGameListView,
    GameDetailView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.GameList, name='game-list'),
    path('games/<int:pk>/', views.GameDetail, name='game-detail'),
    path('games/<int:pk>/reviews/', views.GameReviews, name='game-reviews'),
    path('games/<int:pk>/reviews/<int:search>/', views.GameReviewsContinue, name='game-reviews-continue'),
    path('old-games/<int:pk>/', GameDetailView.as_view(), name='old-game-detail'),
    path('old-games/', OldGameListView.as_view(), name='old-game-list'),
]
