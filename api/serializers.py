from rest_framework import serializers
from home.models import Game, GameStat, Review, Descriptor

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GameStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStat
        fields = '__all__'

class DescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        fields = '__all__'
