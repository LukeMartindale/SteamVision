from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import GameSerializer, GameStatSerializer

from home.models import Game, GameStat, Review


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
