from django.contrib import admin
from . models import Game, GameStat, PlayerCount, Review, Descriptor, Developer

# Register your models here.
admin.site.register(Game)
admin.site.register(GameStat)
admin.site.register(PlayerCount)
admin.site.register(Review)
admin.site.register(Descriptor)
admin.site.register(Developer)
