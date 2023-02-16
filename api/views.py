from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import GameSerializer, GameReviewSerializer, GameStatSerializer, DescriptorSerializer

from home.models import Game, GameStat, Review, Descriptor


# Create your views here.

@api_view(['GET'])
def getAllGames(request):
    game = Game.objects.all()
    serializer = GameSerializer(game, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGame(request, id):

    try:
        game = Game.objects.filter(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameSerializer(game, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getGameStats(request, id):
    game_stats = GameStat.objects.filter(app_id__app_id__contains=id)
    serializer = GameStatSerializer(game_stats, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getReviews(request, id):
    reviews = Review.objects.filter(app_id__app_id__contains=id).order_by("time_created")
    serializer = GameReviewSerializer(reviews, many=True)

    years = [y.year for y in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'year')]
    months = [m.month for m in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'month')]

    print(years)
    print(months)

    return Response({'data': serializer.data, 'years': years, 'months': months})

@api_view(['POST'])
def getReviewsData(request, id):
    game = Game.objects.get(app_id=id)
    stats = GameStat.objects.get(app_id=game)

    if request.data["type"] == "all_time_year":
        return Response(stats.reviews_all_time_year)

    return Response({"test": "test"})

@api_view(['GET'])
def getAllReviews(request):
    temp = { 730: [
        {'label': '-1', 'value': 2}, 
        {'label': '-0.9', 'value': 3}, 
        {'label': '-0.8', 'value': 1}, 
        {'label': '-0.7', 'value': 3}, 
        {'label': '-0.6', 'value': 5}, 
        {'label': '-0.5', 'value': 14}, 
        {'label': '-0.4', 'value': 59}, 
        {'label': '-0.3', 'value': 9}, 
        {'label': '-0.2', 'value': 41}, 
        {'label': '-0.1', 'value': 55}, 
        {'label': '0', 'value': 539}, 
        {'label': '0.1', 'value': 199}, 
        {'label': '0.2', 'value': 141}, 
        {'label': '0.3', 'value': 178}, 
        {'label': '0.4', 'value': 47}, 
        {'label': '0.5', 'value': 99}, 
        {'label': '0.6', 'value': 47}, 
        {'label': '0.7', 'value': 60}, 
        {'label': '0.8', 'value': 21}, 
        {'label': '0.9', 'value': 13}, 
        {'label': '1', 'value': 64},
    ]}
    return Response(temp)

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
