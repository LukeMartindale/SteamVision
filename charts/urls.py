from django.urls import path
from . views import (
    GameTopView
)

urlpatterns = [
    path('', GameTopView.as_view(), name='game-charts')
]
