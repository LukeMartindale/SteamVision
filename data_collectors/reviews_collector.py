import requests
import urllib.parse

from home.models import Review, Game, GameStat
from data_processors.reviews_sentiment import reviews_sentiment
from data_processors.reviews_emotions import reviews_emotions
from datetime import datetime
from django.utils import timezone

import os

def initial_reviews_collector(game_id):
    #get game object
    game = Game.objects.get(app_id=game_id)

    if(game):
        api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all".format(game_id)
        response_reviews = requests.get(api_url).json()

        total = response_reviews["query_summary"]["total_reviews"]
        current = 0

        on_read_sentiment = (os.environ.get('ON_READ_SENTIMENT') == 'True')
        on_read_emotion = (os.environ.get('ON_READ_EMOTION') == 'True')

        while response_reviews["reviews"]:
            for i in range(len(response_reviews["reviews"])):

                #Check if review has already been read into database
                if Review.objects.filter(review_id=response_reviews["reviews"][i]["recommendationid"]).exists():
                    print(response_reviews["reviews"][i]["recommendationid"])
                    return {"status": 200, "message": "Collection finished"}
                else:
                    current+=1
                    print(current, " / ", total)
                    
                    review = Review()

                    review.app_id = game
                    review.review_id = response_reviews["reviews"][i]["recommendationid"]
                    review.author_id = response_reviews["reviews"][i]["author"]["steamid"]

                    review.language = response_reviews["reviews"][i]["language"]
                    review.review_text = response_reviews["reviews"][i]["review"]

                    review.time_created = datetime.fromtimestamp(response_reviews["reviews"][i]["timestamp_created"])
                    if response_reviews["reviews"][i]["author"].get("playtime_at_review"):review.playtime_at_review = response_reviews["reviews"][i]["author"]["playtime_at_review"]

                    if(on_read_sentiment):
                        sentiment = reviews_sentiment(response_reviews["reviews"][i]["review"])
                        review.sentiment_pos = sentiment["positive"]
                        review.sentiment_polarity = sentiment["polarity"]
                        review.sentiment_subjectivity = sentiment["subjectivity"]

                    if(on_read_emotion):
                        emotions = reviews_emotions(response_reviews["reviews"][i]["review"])
                        review.emotion_scores = emotions["scores"]
                        review.emotion_prominent = emotions["prominent"]

                    review.voted_up = response_reviews["reviews"][i]["voted_up"]
                    review.votes_up = response_reviews["reviews"][i]["votes_up"]
                    review.votes_funny = response_reviews["reviews"][i]["votes_funny"]

                    review.purchase_on_steam = response_reviews["reviews"][i]["steam_purchase"]
                    review.received_for_free = response_reviews["reviews"][i]["received_for_free"]
                    review.written_during_early_access = response_reviews["reviews"][i]["written_during_early_access"]

                    review.save()

            next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all&cursor={}".format(game_id, urllib.parse.quote(response_reviews["cursor"]))
            response_reviews = requests.get(next_url).json()

        return {"status": 200, "message": "Collection successful"}
    else:
        return {"status": 400, "message": "This app does not exist!"}

def initial_reviews_collector_continue(game_id, cursor):
    #get game object
    game = Game.objects.get(app_id=game_id)

    num_reviews = False

    if(game):

        if(cursor):
            api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all&cursor={}".format(game_id, urllib.parse.quote(cursor))
            response_reviews = requests.get(api_url).json()
            total = response_reviews["query_summary"]["num_reviews"]
            num_reviews = True
        else:
            api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all".format(game_id)
            response_reviews = requests.get(api_url).json()
            total = response_reviews["query_summary"]["total_reviews"]

        current = 0

        on_read_sentiment = (os.environ.get('ON_READ_SENTIMENT') == 'True')
        on_read_emotion = (os.environ.get('ON_READ_EMOTION') == 'True')

        if(on_read_sentiment):
            print("SENTIMENT TRUE")
        if(on_read_emotion):
            print("EMOTION TRUE")

        while response_reviews["reviews"]:
            for i in range(len(response_reviews["reviews"])):

                #Check if review has already been read into database
                if Review.objects.filter(review_id=response_reviews["reviews"][i]["recommendationid"]).exists():
                    current+=1
                    print(current, " / ", total, " - Pass")
                else:
                    current+=1
                    print(current, " / ", total)
                    
                    review = Review()

                    review.app_id = game
                    review.review_id = response_reviews["reviews"][i]["recommendationid"]
                    review.author_id = response_reviews["reviews"][i]["author"]["steamid"]

                    review.language = response_reviews["reviews"][i]["language"]
                    review.review_text = response_reviews["reviews"][i]["review"]

                    review.time_created = datetime.fromtimestamp(response_reviews["reviews"][i]["timestamp_created"])
                    if response_reviews["reviews"][i]["author"].get("playtime_at_review"):review.playtime_at_review = response_reviews["reviews"][i]["author"]["playtime_at_review"]

                    if(on_read_sentiment):
                        sentiment = reviews_sentiment(response_reviews["reviews"][i]["review"])
                        review.sentiment_pos = sentiment["positive"]
                        review.sentiment_polarity = sentiment["polarity"]
                        review.sentiment_subjectivity = sentiment["subjectivity"]

                    if(on_read_emotion):
                        emotions = reviews_emotions(response_reviews["reviews"][i]["review"])
                        review.emotion_scores = emotions["scores"]
                        review.emotion_prominent = emotions["prominent"]

                    review.voted_up = response_reviews["reviews"][i]["voted_up"]
                    review.votes_up = response_reviews["reviews"][i]["votes_up"]
                    review.votes_funny = response_reviews["reviews"][i]["votes_funny"]

                    review.purchase_on_steam = response_reviews["reviews"][i]["steam_purchase"]
                    review.received_for_free = response_reviews["reviews"][i]["received_for_free"]
                    review.written_during_early_access = response_reviews["reviews"][i]["written_during_early_access"]

                    review.save()

            print(response_reviews["cursor"])

            next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all&cursor={}".format(game_id, urllib.parse.quote(response_reviews["cursor"]))
            response_reviews = requests.get(next_url).json()
            if(num_reviews):
                total += response_reviews["query_summary"]["num_reviews"]

        return {"status": 200, "message": "Collection successful"}
    else:
        return {"status": 400, "message": "This app does not exist!"}

def reviews_new_all_collector():
    games = Game.objects.all()

    on_read_sentiment = (os.environ.get('ON_READ_SENTIMENT') == 'True')
    on_read_emotion = (os.environ.get('ON_READ_EMOTION') == 'True')

    for game in games:
        
        api_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all".format(game.app_id)
        response_reviews = requests.get(api_url).json()

        no_new = False

        while response_reviews["reviews"]:
            for i in range(len(response_reviews["reviews"])):
                if Review.objects.filter(review_id=response_reviews["reviews"][i]["recommendationid"]).exists():
                    no_new = True
                else:
                    review = Review()

                    review.app_id = game
                    review.review_id = response_reviews["reviews"][i]["recommendationid"]
                    review.author_id = response_reviews["reviews"][i]["author"]["steamid"]

                    review.language = response_reviews["reviews"][i]["language"]
                    review.review_text = response_reviews["reviews"][i]["review"]

                    review.time_created = datetime.fromtimestamp(response_reviews["reviews"][i]["timestamp_created"])
                    if response_reviews["reviews"][i]["author"].get("playtime_at_review"):review.playtime_at_review = response_reviews["reviews"][i]["author"]["playtime_at_review"]

                    if(on_read_sentiment):
                        sentiment = reviews_sentiment(response_reviews["reviews"][i]["review"])
                        review.sentiment_pos = sentiment["positive"]
                        review.sentiment_polarity = sentiment["polarity"]
                        review.sentiment_subjectivity = sentiment["subjectivity"]

                    if(on_read_emotion):
                        emotions = reviews_emotions(response_reviews["reviews"][i]["review"])
                        review.emotion_scores = emotions["scores"]
                        review.emotion_prominent = emotions["prominent"]

                    review.voted_up = response_reviews["reviews"][i]["voted_up"]
                    review.votes_up = response_reviews["reviews"][i]["votes_up"]
                    review.votes_funny = response_reviews["reviews"][i]["votes_funny"]

                    review.purchase_on_steam = response_reviews["reviews"][i]["steam_purchase"]
                    review.received_for_free = response_reviews["reviews"][i]["received_for_free"]
                    review.written_during_early_access = response_reviews["reviews"][i]["written_during_early_access"]

                    review.save()

                if no_new:
                    break
            if no_new:
                break

            next_url = "https://store.steampowered.com/appreviews/{}?json=1&filter=recent&purchase_type=all&cursor={}".format(game.app_id, urllib.parse.quote(response_reviews["cursor"]))
            response_reviews = requests.get(next_url).json()

        # Calculate Review Score & update highest review score if needed
        game_stats = GameStat.objects.get(app_id=game)
        game_reviews = Review.objects.filter(app_id=game).count()
        game_reviews_up = Review.objects.filter(app_id=game, voted_up=True).count()

        print(game_reviews)
        print(game_reviews_up)

        print(len(Review.objects.filter(app_id=game)))
        print(len(Review.objects.filter(app_id=game, voted_up=True)))

        review_score = game_reviews_up / game_reviews
        print(review_score)
        game_stats.current_review_score = review_score



        if(review_score > game_stats.highest_review_score):
            game_stats.highest_review_score = review_score
            game_stats.highest_review_score_date = timezone.now()

        game_stats.save()

    return {"status": 200, "message": "Collection successful"}
