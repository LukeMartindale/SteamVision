from home.models import Review, Game
import requests
import urllib.parse

from datetime import datetime

def initial_reviews_collector(game_id):
    #get game object
    game = Game.objects.get(app_id=game_id)

    if(game):
        api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent".format(game_id)
        response_reviews = requests.get(api_url).json()

        while response_reviews["reviews"]:
            for i in range(len(response_reviews["reviews"])):
                #Check if review has already been read into database
                if Review.objects.filter(review_id=response_reviews["reviews"][i]["recommendationid"]).exists():
                    return {"status": 200, "message": "Collection finished"}
                else:

                    review = Review()

                    review.app_id = game
                    review.review_id = response_reviews["reviews"][i]["recommendationid"]
                    review.author_id = response_reviews["reviews"][i]["author"]["steamid"]

                    review.language = response_reviews["reviews"][i]["language"]
                    review.review_text = response_reviews["reviews"][i]["review"]

                    review.time_created = datetime.fromtimestamp(response_reviews["reviews"][i]["timestamp_created"])
                    if response_reviews["reviews"][i]["author"].get("playtime_at_review"):review.playtime_at_review = response_reviews["reviews"][i]["author"]["playtime_at_review"]

                    review.voted_up = response_reviews["reviews"][i]["voted_up"]
                    review.votes_up = response_reviews["reviews"][i]["votes_up"]
                    review.votes_funny = response_reviews["reviews"][i]["votes_funny"]

                    review.purchase_on_steam = response_reviews["reviews"][i]["steam_purchase"]
                    review.received_for_free = response_reviews["reviews"][i]["received_for_free"]
                    review.written_during_early_access = response_reviews["reviews"][i]["written_during_early_access"]

                    review.save()

            next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&cursor={}".format(game_id, urllib.parse.quote(response_reviews["cursor"]))
            response_reviews = requests.get(next_url).json()

        return {"status": 200, "message": "Collection successful"}
    else:
        return {"status": 400, "message": "This app does not exist!"}