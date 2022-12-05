from django.shortcuts import render
from . import reviews_sentiment_analysis
from . models import Game
from django.views.generic import (
    ListView,
    DetailView,
)

# Create your views here.

temp = [
    {
        'label': '1',
        'value': '10'
    }
]

def home(request):
    return render(request, 'home/base.html', {"tests": Game.objects.all()})

def games(request):

    # context = {
    #     'sentiment': reviews_sentiment_analysis.get_sentiment(reviews_sentiment_analysis.url)
    # }


    return render(request, 'home/game.html')

class GameListView(ListView):
    model = Game
    template_name = 'home/game_list.html'
    context_object_name = 'games'

    # my_function("730")

class GameDetailView(DetailView):
    model = Game
    template_name: str = 'home/game_detail.html'
    context_object_name: str = 'games'


def test(request):

    context = {
        'data': temp
    }

    print(context)

    return render(request, 'home/test.html', {'tests': Game.objects.all(), 'data': temp})
