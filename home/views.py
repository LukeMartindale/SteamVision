from django.shortcuts import render
from . import reviews_sentiment_analysis

# Create your views here.

def home(request):
    return render(request, 'home/base.html')

def games(request):

    sentiment = reviews_sentiment_analysis.get_sentiment(reviews_sentiment_analysis.url)

    data = {'sentiment': sentiment}

    return render(request, 'home/game.html', context=data)

def test(request):
    return render(request, 'home/test.html')
