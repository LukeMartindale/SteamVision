from home.models import Review
from datetime import datetime
from home.models import Game, Review

def getReviews(game_id):

    api_url = "https://store.steampowered.com/appreviews/{}?json=1".format(game_id)

    timestamp = 1669384225
    dt = datetime.fromtimestamp(timestamp)
