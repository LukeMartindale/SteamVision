from home.models import Game, GameStat, PlayerCount
import requests
from django.utils import timezone

def player_count_all_collector():

    games = Game.objects.all()

    time = timezone.now()

    for game in games:
        api_url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={}".format(game.app_id)
        response = requests.get(api_url).json()

        playerCount = PlayerCount()

        playerCount.app_id = game
        playerCount.player_count = response["response"]["player_count"]
        playerCount.timestamp = time

        game_stats = GameStat.objects.get(app_id=game)
        
        if game_stats.highest_player_count < playerCount.player_count:
            game_stats.highest_player_count = playerCount.player_count
            game_stats.save()

        playerCount.save()
