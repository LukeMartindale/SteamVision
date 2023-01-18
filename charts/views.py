from django.shortcuts import render
from home.models import Game
from django.views.generic import (
    ListView
)

# Create your views here.

class GameTopView(ListView):
    model = Game
    template_name = 'charts/game_charts.html'
    context_object_name = 'games'
