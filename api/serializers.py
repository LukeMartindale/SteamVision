from rest_framework import serializers
from home.models import Game, Review

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
