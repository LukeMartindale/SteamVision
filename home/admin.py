from django.contrib import admin
from . models import Game, GameStat, Review

# Register your models here.
admin.site.register(Game)
admin.site.register(GameStat)
admin.site.register(Review)
