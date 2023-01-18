from home.models import Review, Game
import requests
import urllib.parse

from datetime import datetime

def initial_reviews_collector(game_id):

    #get game object
    game = Game.objects.filter(app_id=game_id)

    if(game.first()):

        api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent".format(game_id)
        response_reviews = requests.get(api_url).json()

        while response_reviews["reviews"]:

            for i in range(len(response_reviews["reviews"])):

                review = Review()

                print("TEST 1")
                review.app_id = game.first()
                print("TEST app_id")
                print(review.app_id)
                review.review_id = response_reviews["reviews"][i]["recommendationid"]
                print("TEST review_id")
                print(review.review_id)
                review.author_id = response_reviews["reviews"][i]["author"]["steamid"]
                print("TEST author_id")
                print(review.author_id)

                print("TEST 2")
                review.language = response_reviews["reviews"][i]["language"]
                review.review_text = response_reviews["reviews"][i]["review"]

                print("TEST 3")
                review.time_created = datetime.fromtimestamp(response_reviews["reviews"][i]["timestamp_created"])
                print("TEST time created")
                print(review.time_created)
                if response_reviews["reviews"][i]["author"].get("playtime_at_review"):review.playtime_at_review = response_reviews["reviews"][i]["author"]["playtime_at_review"]
                print("TEST playtime at review")
                print(review.playtime_at_review)

                review.voted_up = response_reviews["reviews"][i]["voted_up"]
                print("TEST voted up")
                print(review.voted_up)
                review.votes_up = response_reviews["reviews"][i]["votes_up"]
                print("TEST votes up")
                print(review.voted_up)
                review.votes_funny = response_reviews["reviews"][i]["votes_funny"]
                print("TEST votes funny")
                print(review.votes_funny)

                review.purchase_on_steam = response_reviews["reviews"][i]["steam_purchase"]
                review.received_for_free = response_reviews["reviews"][i]["received_for_free"]
                review.written_during_early_access = response_reviews["reviews"][i]["written_during_early_access"]

                review.save()

            next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&cursor={}".format(game_id, urllib.parse.quote(response_reviews["cursor"]))
            response_reviews = requests.get(next_url).json()

        return {"status": 200, "message": "Collection successful"}
    else:
        return {"status": 400, "message": "This app does not exist!"}