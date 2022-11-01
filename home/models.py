from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.TextField()


class Review(models.Model):
    steam_id = models.ForeignKey(Game, on_delete=models.CASCADE)
