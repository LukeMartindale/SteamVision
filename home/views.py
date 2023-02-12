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

        games = Game.objects.filter(name__contains=request.POST["search"])

        print(games)

        if(request.POST["genres"]):

            genres = request.POST["genres"].split(",")
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.genres for g in genres)):
                    filtered_games.append(game)

            games = filtered_games

        if(request.POST["tags"]):

            tags = request.POST["tags"].split(",")
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.tags for g in tags)):
                    filtered_games.append(game)

            games = filtered_games

        if(request.POST["categories"]):

            categories = request.POST["categories"].split(",")
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.categories for g in categories)):
                    filtered_games.append(game)

            games = filtered_games

        context = {"games": games, "descriptors": descriptors}

    else:
        context = {"games": Game.objects.all(), "descriptors": descriptors}

    return render(request, 'home/game-list.html', context)

def GameDetail(request, pk):

    game = Game.objects.get(app_id=pk)

    descriptors = Descriptor.objects.all().order_by('name').values()

    context = {'game': game, 'descriptors': descriptors}

    return render(request, 'home/game-detail.html', context)

class OldGameListView(ListView):
    model = Game
    template_name = 'home/old_game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/old_game_detail.html'
    context_object_name: str = 'games'
