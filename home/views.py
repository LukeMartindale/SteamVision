from django.shortcuts import render, redirect
from . models import Game, GameStat, Descriptor, Review, PlayerCount, Developer
from django.views.generic import (
    ListView,
    DetailView,
)

from django.core.paginator import Paginator
import re

import time

from .views_helper import (
    reviews_score_search_filter_value,
    sentiment_score_search_filter_value,
    emotion_prominent_search_filter_value
)

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def GameList(request):

    descriptors = Descriptor.objects.all().order_by('name').values()

    pass_search = False
    searchtextParams = ""
    genresParams = ""
    tagsParams = ""
    categoriesParams = ""
    
    # If user has posted from the filter form
    if request.method == "POST":

        print("POST")
        pass_search = True

        games = Game.objects.filter(name__icontains=request.POST["search"]).order_by('name')
        searchtextParams = request.POST["search"]

        if(request.POST["genres"]):

            genres = request.POST["genres"].split(",")
            genresParams = request.POST["genres"]
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.genres for g in genres)):
                    filtered_games.append(game)

            games = filtered_games

        if(request.POST["tags"]):

            tags = request.POST["tags"].split(",")
            tagsParams = request.POST["tags"]
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.tags for g in tags)):
                    filtered_games.append(game)

            games = filtered_games

        if(request.POST["categories"]):

            categories = request.POST["categories"].split(",")
            categoriesParams =  request.POST["categories"]
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.categories for g in categories)):
                    filtered_games.append(game)

            games = filtered_games

    elif request.GET.get('search_text', False) or request.GET.get('genres', False) or request.GET.get('tags', False) or request.GET.get('categories', False):
        print("GET")
        print(request.GET.get('search_text', False))
        print(request.GET.get('genres', False))
        pass_search = True
        games = Game.objects.filter(name__contains=request.GET.get('search_text', False))
        searchtextParams = request.GET.get('search_text', False)

        if(request.GET.get('genres', False)):

            genres = request.GET.get('genres', False).split(",")
            genresParams = request.GET.get('genres', False)
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.genres for g in genres)):
                    filtered_games.append(game)

            games = filtered_games



        if(request.GET.get('tags', False)):

            tags = request.GET.get('tags', False).split(",")
            tagsParams = request.GET.get('tags', False)
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.tags for g in tags)):
                    filtered_games.append(game)

            games = filtered_games



        if(request.GET.get('categories', False)):

            categories = request.GET.get('categories', False).split(",")
            categoriesParams = request.GET.get('categories', False)
            filtered_games = []

            for index, game in enumerate(games):
                if(all(g in game.categories for g in categories)):
                    filtered_games.append(game)

            games = filtered_games

    else:
        print("ELSE")
        games =  Game.objects.all().order_by("name")

    paginator = Paginator(games, 10)
    page_number = request.GET.get('page')
    paginated_games = paginator.get_page(page_number)

    context = {
        "games": paginated_games, 
        "descriptors": descriptors,
        "pass_search": pass_search,
        "search_text": searchtextParams, 
        "genres": genresParams,
        "tags": tagsParams,
        "categories": categoriesParams
    }

    return render(request, 'home/game-list.html', context)

def GameDetail(request, pk):

    game = Game.objects.get(app_id=pk)
    game_stats = GameStat.objects.get(app_id__app_id=pk)
    developers = Developer.objects.filter(name__in=game.developer)
    descriptors = Descriptor.objects.all().order_by('name').values()
    player_count = PlayerCount.objects.filter(app_id=game).last()
    sentiment_score = GameStat.objects.get(app_id=game).current_sentiment_score

    #Order developers into the correct order 
    ordered_developers = []
    for dev in game.developer:
        for devs in developers:
            if dev == devs.name:
                ordered_developers.append(devs)

    reviews_format = ["[list]", "[/list]", "[i]", "[/i]", "[b]", "[/b]", "[h1]", "[/h1]", "[code]", "[/code]", "[/url]", "[spoiler]", "[/spoiler]"]
    reg = "\[url=[^\]]*]"

    reviews = Review.objects.filter(app_id=game).order_by('-time_created')

    reviews = reviews[0:10]

    # Formated reviews by removing unecceseray content
    for review in reviews:
        for format in reviews_format:
            review.review_text = review.review_text.replace(format, '')

    for review in reviews:
        review.review_text = re.sub(reg, '', review.review_text)

    context = {
        'game': game, 
        'game_stats': game_stats, 
        'developers': ordered_developers,
        'player_count': player_count, 
        'descriptors': descriptors,
        'sentiment_score': sentiment_score, 
        "reviews": reviews
        }
    
    return render(request, 'home/game-detail.html', context)

def GameReviews(request, pk):

    # Get game data and set pass through variables 
    game = Game.objects.get(app_id=pk)
    pass_search = False
    search_text = ""
    review_score = ""
    sentiment_range = ""
    prominent_emotion = ""

    reviews_format = ["[list]", "[/list]", "[i]", "[/i]", "[b]", "[/b]", "[h1]", "[/h1]", "[code]", "[/code]", "[/url]", "[spoiler]", "[/spoiler]"]
    reg = "\[url=[^\]]*]"

    if request.method == 'POST':

        reviews_filter = reviews_score_search_filter_value(request.POST["review-score-select"])
        sentiment_filter = sentiment_score_search_filter_value(request.POST["sentiment-range-select"])
        emotion_filter = emotion_prominent_search_filter_value(request.POST["prominent-emotion-select"])

        # GET reviews 
        reviews = Review.objects.filter(
            app_id=game, 
            review_text__icontains=request.POST["reviews-search-text"],
            voted_up__in=reviews_filter,
            sentiment_polarity__lte=sentiment_filter["top-range"], 
            sentiment_polarity__gte=sentiment_filter["bottom-range"],
            emotion_prominent__icontains=emotion_filter,
        ).order_by('time_created')
        
        # SET pass through variables
        pass_search = True
        search_text = request.POST["reviews-search-text"]
        review_score = request.POST["review-score-select"]
        sentiment_range = request.POST["sentiment-range-select"]
        prominent_emotion = request.POST["prominent-emotion-select"]

    elif request.GET.get('search_text', False) or request.GET.get('review_score', False) or request.GET.get('sentiment_range', False) or request.GET.get('prominent_emotion', False):

        reviews_filter = reviews_score_search_filter_value(request.GET.get('review_score', False))
        sentiment_filter = sentiment_score_search_filter_value(request.GET.get('sentiment_range', False))
        emotion_filter = emotion_prominent_search_filter_value(request.GET.get('prominent_emotion', False))

        # GET reviews
        reviews = Review.objects.filter(
            app_id=game, 
            review_text__contains=request.GET.get('search_text', False),
            voted_up__in=reviews_filter,
            sentiment_polarity__lte=sentiment_filter["top-range"], 
            sentiment_polarity__gte=sentiment_filter["bottom-range"],
            emotion_prominent__icontains=emotion_filter,
        ).order_by('time_created')

        # SET pass through variables
        pass_search = True
        search_text = request.GET.get('search_text', False)
        review_score = request.GET.get('review_score', False)
        sentiment_range = request.GET.get('sentiment_range', False)
        prominent_emotion = request.GET.get('prominent_emotion', False)

    else:
        reviews = Review.objects.filter(app_id=game).order_by('-time_created')

    # Formated reviews by removing unecceseray content
    # for review in reviews:
    #     for format in reviews_format:
    #         review.review_text = review.review_text.replace(format, '')

    # for review in reviews:
    #     review.review_text = re.sub(reg, '', review.review_text)

    paginator = Paginator(reviews, 20)
    page_number = request.GET.get('page')
    paginated_reviews = paginator.get_page(page_number)

    context = {'game': game, 'reviews': paginated_reviews, 'pass_search': pass_search, "search_text": search_text, "review_score": review_score, "sentiment_range": sentiment_range, "prominent_emotion": prominent_emotion}

    return render(request, 'home/game-reviews.html', context)
