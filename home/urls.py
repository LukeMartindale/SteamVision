from django.urls import path
from . import views
from . views import (
    GameListView,
    GameDetailView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('games/', GameListView.as_view(), name='game-list'),
]
