from home.models import Review, Game
import requests
import urllib.parse

from datetime import datetime

def initial_reviews_collector(game_id):
    api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent".format(game_id)
    response_reviews = requests.get(api_url).json()
    print(response_reviews["reviews"][0])

    game = Game.objects.filter(app_id=game_id)



    review = Review()

    review.app_id = game.first()
    review.review_id = response_reviews["reviews"][0]["recommendationid"]
    review.author_id = response_reviews["reviews"][0]["author"]["steamid"]

    review.time_created = datetime.fromtimestamp(response_reviews["reviews"][0]["timestamp_created"])

    print(game[0].app_id)
    print(review.app_id)
    print(review.review_id)
    print(review.author_id)
    print(review.time_created)


    # while(response_reviews["reviews"]):

    #     review = Review()

    #     review.app_id = game_id

    #     next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&cursor={}".format(game_id, urllib.parse.quote(response_reviews["cursor"]))
    #     response_reviews = requests.get(next_url).json()
