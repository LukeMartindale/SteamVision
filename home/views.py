from django.shortcuts import render
from . import reviews_sentiment_analysis
from . models import Game
from django.views.generic import (
    ListView,
    DetailView,
)

from helper_files.addGame import getGame
from helper_files.getReviews import getReviews, getReviewsStats

# Create your views here.

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def games(request):

    return render(request, 'home/game.html')

class GameListView(ListView):
    model = Game
    template_name = 'home/game_list.html'
    context_object_name = 'games'

    # getGame("10")
    # getReviews("10")
    # getReviewsStats("10")

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/game_detail.html'
    context_object_name: str = 'games'


def test(request):

    return render(request, 'home/test.html')
