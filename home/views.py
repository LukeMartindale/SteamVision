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
    pass_search = False
    search_text = None
    review_score = None
    sentiment_range = None
    prominent_range = None

    reviews_format = ["[list]", "[/list]", "[i]", "[/i]", "[b]", "[/b]", "[h1]", "[/h1]", "[code]", "[/code]", "[/url]", "[spoiler]", "[/spoiler]"]
    reg = "\[url=[^\]]*]"

    # options = {
    #     "text": , 
    #     "review_score": request.POST["review-score-select"], 
    #     "sentiment_score": request.POST["sentiment-range-select"],
    #     "prominent_emotion": request.POST["prominent-emotion-select"],
    # }
    # print(options)

    if request.method == 'POST':
        reviews = Review.objects.filter(app_id=game, review_text__contains=request.POST["reviews-search-text"]).order_by('time_created')
        pass_search = True
        search_text = request.POST["reviews-search-text"]
        review_score = request.POST["review-score-select"]
        sentiment_range = request.POST["sentiment-range-select"]
        prominent_range = request.POST["prominent-emotion-select"]
    elif request.GET.get('search_text', False) or request.GET.get('reviews_score', False):
        print("IN")
        reviews = Review.objects.filter(
            app_id=game, 
            review_text__contains=request.GET.get('search_text'),
        ).order_by('time_created')
        pass_search = True
        search_text = request.GET.get('search_text', False)
        review_score = request.GET.get('reviews_score', False)
        sentiment_range = request.GET.get('sentiment_range', False)
        prominent_range = request.GET.get('prominent_range', False)
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
    paginated_reviews = paginator.get_page(page_number)

    context = {'game': game, 'reviews': paginated_reviews, 'pass_search': pass_search}

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
