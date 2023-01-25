from home.models import Game, PlayerCount
import requests
from datetime import datetime
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

        playerCount.save()
