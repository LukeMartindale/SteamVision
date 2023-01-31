from django.shortcuts import render
from . models import Game
from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def GameList(request):
    if request.method == "POST":
        print(request.POST)
        # print(request.POST["tags"])
        # print(type(request.POST["tags"]))
        # test = request.POST["tags"].split(",")
        # print(test)
        context = {"games": Game.objects.filter(name__contains=request.POST["search"])}
    else:
        context = {"games": Game.objects.all()}



    return render(request, 'home/game-list.html', context)

class OldGameListView(ListView):
    model = Game
    template_name = 'home/old_game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/game_detail.html'
    context_object_name: str = 'games'
