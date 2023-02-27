from django.shortcuts import render
from django.db.models import Max
from home.models import Game, GameStat, PlayerCount

# Create your views here.

def Charts(request):
    games = Game.objects.all()

    # Get List of current most played games
    players_current = []
    for game in games:

        current = {}
        player_count = PlayerCount.objects.filter(app_id=game).last()

        current["app"] = game
        current["player_count"] = player_count.player_count
        players_current.append(current)

    players_current = sorted(players_current, key=lambda x:x['player_count'], reverse=True)

    return render(request, 'charts/charts.html', {"players_current": players_current})