from django.urls import path
from . import views

urlpatterns = [
    path('get-games/', views.getAllGames),
    path('get-games/<int:id>/', views.getGame),
    path('get-games-stats/<int:id>/', views.getGameStats),
    path('get-reviews/<int:id>/', views.getReviews),
    path('get-descriptors/', views.getDescriptors),
    path('get-genres/', views.getGenres),
    path('get-tags/', views.getTags),
    path('get-categories/', views.getCategories),
]