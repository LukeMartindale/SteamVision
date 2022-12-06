from rest_framework import serializers
from home.models import Game, Review, ReviewsStat

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class ReviewStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsStat
        fields = '__all__'
