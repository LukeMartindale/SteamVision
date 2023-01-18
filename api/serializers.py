from rest_framework import serializers
from home.models import Game, GameStat, Review

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStat
        fields = '__all__'
