from django.urls import path
from . import views

urlpatterns = [
    path('get-games/', views.getAllGames),
    path('get-games/<int:id>/', views.getGame),
    path('get-games-stats/<int:id>/', views.getGameStats),
    path('get-reviews/all-time-year/<int:id>/', views.getReviewsAllTimeYear),
    path('get-reviews/all-time-month/<int:id>/', views.getReviewsAllTimeMonth),
    path('get-reviews/past-twelve-months/<int:id>/', views.getReviewsPastTweleveMonths),
    path('get-reviews/past-six-months/<int:id>/', views.getReviewsPastSixMonths),
    path('get-reviews/past-one-month/<int:id>/', views.getReviewsPastOneMonth),
    path('get-reviews/past-two-weeks/<int:id>/', views.getReviewsPastTwoWeeks),
    path('get-reviews/past-one-week/<int:id>/', views.getReviewsPastOneWeek),
    path('get-descriptors/', views.getDescriptors),
    path('get-genres/', views.getGenres),
    path('get-tags/', views.getTags),
    path('get-categories/', views.getCategories),
]