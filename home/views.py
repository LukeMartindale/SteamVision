from django.shortcuts import render, redirect
from . models import Game, GameStat, Descriptor, Review
from django.views.generic import (
    ListView,
    DetailView,
)

from django.core.paginator import Paginator
import re

# Create your views here.

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def GameList(request):

    descriptors = Descriptor.objects.all().order_by('name').values()

    if request.method == "POST":

        games = Game.objects.filter(name__contains=request.POST["search"])

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

    total_reviews = len(Review.objects.filter(app_id=game))
    sentiment_score = GameStat.objects.get(app_id=game).current_sentiment_score

    context = {'game': game, 'descriptors': descriptors, 'total_reviews': total_reviews, 'sentiment_score': sentiment_score}

    return render(request, 'home/game-detail.html', context)

def GameReviews(request, pk):

    game = Game.objects.get(app_id=pk)

    reviews_format = ["[list]", "[/list]", "[i]", "[/i]", "[b]", "[/b]", "[h1]", "[/h1]", "[code]", "[/code]", "[/url]", "[spoiler]", "[/spoiler]"]
    reg = "\[url=[^\]]*]"

    if request.method == 'POST':

        # options = {
        #     "text": , 
        #     "review_score": request.POST["review-score-select"], 
        #     "sentiment_score": request.POST["sentiment-range-select"],
        #     "prominent_emotion": request.POST["prominent-emotion-select"],
        # }
        # print(options)

        reviews = Review.objects.filter(app_id=game, review_text__contains=request.POST["reviews-search-text"]).order_by('time_created')

        # Formated reviews by removing unecceseray content
        for review in reviews:
            for format in reviews_format:
                review.review_text = review.review_text.replace(format, '')

        for review in reviews:
            review.review_text = re.sub(reg, '', review.review_text)

        paginator = Paginator(reviews, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'game': game, 'reviews': reviews, 'page_obj': page_obj}

        return redirect()

    else:
        reviews = Review.objects.filter(app_id=game).order_by('time_created')

        # Formated reviews by removing unecceseray content
        for review in reviews:
            for format in reviews_format:
                review.review_text = review.review_text.replace(format, '')

        for review in reviews:
            review.review_text = re.sub(reg, '', review.review_text)

        paginator = Paginator(reviews, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'game': game, 'reviews': reviews, 'page_obj': page_obj}

    return render(request, 'home/game-reviews.html', context)

def GameReviewsContinue(request, pk, search):

    context = {}

    return render(request, 'home/game-reviews.html', context)

class OldGameListView(ListView):
    model = Game
    template_name = 'home/old_game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/old_game_detail.html'
    context_object_name: str = 'games'
