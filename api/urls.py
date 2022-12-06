from django.urls import path
from . import views

urlpatterns = [
    path('get-games/', views.getAllGames),
    path('get-games/<int:id>', views.getGame),
    path('get-reviews/', views.getAllReviews),
    path('get-reviews-stats/<int:id>/', views.getReviewsStats),
]