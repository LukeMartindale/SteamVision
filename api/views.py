from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import GameSerializer, GameReviewSerializer, GameStatSerializer, DescriptorSerializer
from home.models import Game, GameStat, Review, Descriptor
from django.utils import timezone
import datetime
import calendar

# Get a single game by its app_id / pk
@api_view(['GET'])
def getGame(request, id):

    try:
        game = Game.objects.filter(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameSerializer(game, many=True)

    return Response(serializer.data)

# get all games in the database
@api_view(['GET'])
def getAllGames(request):
    game = Game.objects.all()
    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)

# Get a single game stat object by its app_id / pk of the game
@api_view(['GET'])
def getGameStats(request, id):
    game_stats = GameStat.objects.filter(app_id__app_id__contains=id)
    serializer = GameStatSerializer(game_stats, many=True)

    return Response(serializer.data)

# Get the all time year reviews data form game stat object by its app_id / pk of the game
@api_view(['GET'])
def getReviewsAllTimeYear(request, id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)
    
    return Response(stat.reviews_all_time_year)

@api_view(['GET'])
def getReviewsAllTimeMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)

    return Response(stat.reviews_all_time_month)

@api_view(['GET'])
def getReviewsPastTweleveMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id__contains=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.reviews_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 12
    past_twelve_months = []

    for stat in reversed(stats.reviews_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    return Response(past_twelve_months)

@api_view(['GET'])
def getReviewsPastSixMonths(request, id):
    stats = GameStat.objects.get(app_id__app_id__contains=id)

    time = timezone.now()
    end_index = 0

    for index, stat in enumerate(stats.reviews_all_time_month):
        if(stat["year"] == time.year and stat["month"] == calendar.month_name[time.month]):
            end_index = index+1
            break

    start_index = end_index - 6
    past_twelve_months = []

    for stat in reversed(stats.reviews_all_time_month[start_index:end_index]):
        past_twelve_months.append(stat)

    return Response(past_twelve_months)

@api_view(['GET'])
def getReviewsPastOneMonth(request, id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)
    
    return Response(reversed(stat.reviews_past_one_month))

@api_view(['GET'])
def getReviewsPastTwoWeeks(request, id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)
    reviews_percentages = []

    # Get all dates from the last 30 days
    for i in range(0, 14):
        reviews_percentages.append(stat.reviews_past_one_month[i])

    return Response(reversed(reviews_percentages))

@api_view(['GET'])
def getReviewsPastOneWeek(request, id):
    stat = GameStat.objects.get(app_id__app_id__contains=id)
    reviews_percentages = []

    # Get all dates from the last 30 days
    for i in range(0, 7):
        reviews_percentages.append(stat.reviews_past_one_month[i])

    return Response(reversed(reviews_percentages))

@api_view(['GET'])
def getDescriptors(request):
    descriptors = Descriptor.objects.all()
    serializer = DescriptorSerializer(descriptors, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getGenres(request):
    genres = Descriptor.objects.filter(type="Genres")
    serializer = DescriptorSerializer(genres, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getTags(request):
    tags = Descriptor.objects.filter(type="Tags")
    serializer = DescriptorSerializer(tags, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Descriptor.objects.filter(type="Categories")
    serializer = DescriptorSerializer(categories, many=True)

    return Response(serializer.data)
