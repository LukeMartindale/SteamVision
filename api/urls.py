from django.urls import path
from . import views

urlpatterns = [
    path('get-games/', views.getAllGames),
    path('get-games/<int:id>/', views.getGame),
    path('get-games-stats/<int:id>/', views.getGameStats),
    path('get-reviews/all-time-year/<int:id>/', views.getReviewsAllTimeYear),
    path('get-reviews/all-time-month/<int:id>/', views.getReviewsAllTimeMonth),
    path('get-reviews/past-twelve-months/<int:id>/', views.getReviewsPastTwelveMonths),
    path('get-reviews/past-six-months/<int:id>/', views.getReviewsPastSixMonths),
    path('get-reviews/past-one-month/<int:id>/', views.getReviewsPastOneMonth),
    path('get-reviews/past-two-weeks/<int:id>/', views.getReviewsPastTwoWeeks),
    path('get-reviews/past-one-week/<int:id>/', views.getReviewsPastOneWeek),
    path('get-sentiment/all-time/<int:id>/', views.getSentimentAllTime),
    path('get-sentiment/all-time-month/<int:id>/', views.getSentimentAllTimeMonth),
    path('get-sentiment/past-twelve-months/<int:id>/', views.getSentimentPastTwelveMonths),
    path('get-sentiment/past-six-months/<int:id>/', views.getSentimentPastSixMonths),
    path('get-sentiment/past-one-month/<int:id>/', views.getSentimentPastOneMonth),
    path('get-sentiment/past-two-weeks/<int:id>/', views.getSentimentPastTwoWeeks),
    path('get-sentiment/past-one-week/<int:id>/', views.getSentimentPastOneWeek),
    path('get-emotion/all-time/<int:id>/', views.getEmotionAllTime),
    path('get-emotion/all-time-month/<int:id>/', views.getEmotionAllTimeMonth),
    path('get-emotion/past-twelve-months/<int:id>/', views.getEmotionPastTwelveMonths),
    path('get-emotion/past-six-months/<int:id>/', views.getEmotionPastSixMonths),
    path('get-emotion/past-one-month/<int:id>/', views.getEmotionPastOneMonth),
    path('get-emotion/past-two-weeks/<int:id>/', views.getEmotionPastTwoWeeks),
    path('get-emotion/past-one-week/<int:id>/', views.getEmotionPastOneWeek),
    path('get-descriptors/', views.getDescriptors),
    path('get-genres/', views.getGenres),
    path('get-tags/', views.getTags),
    path('get-categories/', views.getCategories),
    path('get-player-count/past-one-month/<int:id>/', views.getPlayerCountPastOneMonth),
    path('get-player-count/past-two-weeks/<int:id>/', views.getPlayerCountPastTwoWeeks),
    path('get-player-count/past-one-week/<int:id>/', views.getPlayerCountPastOneWeek),
    path('get-player-count/past-72-hours/<int:id>/', views.getPlayerCountPast72Hours),
    path('get-player-count/past-48-hours/<int:id>/', views.getPlayerCountPast48Hours),
    path('get-player-count/past-24-hours/<int:id>/', views.getPlayerCountPast24Hours),
]