from django.shortcuts import render
from . models import Game, Descriptor
from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def GameList(request):

    descriptors = Descriptor.objects.all().order_by('name').values()

    if request.method == "POST":
        print(request.POST)
        games = Game.objects.filter(name__contains=request.POST["search"])
        print(games)
        context = {"games": games, "descriptors": descriptors }
    else:
        context = {"games": Game.objects.all(), "descriptors": descriptors}

    return render(request, 'home/game-list.html', context)

class OldGameListView(ListView):
    model = Game
    template_name = 'home/old_game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/game_detail.html'
    context_object_name: str = 'games'
