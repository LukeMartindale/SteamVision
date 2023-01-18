from django.shortcuts import render
from . models import Game
from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def games(request):

    return render(request, 'home/game.html')

class GameListView(ListView):
    model = Game
    template_name = 'home/game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/game_detail.html'
    context_object_name: str = 'games'


def test(request):

    return render(request, 'home/test.html')
