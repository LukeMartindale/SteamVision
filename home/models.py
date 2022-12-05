from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    app_id = models.IntegerField(default=0, primary_key=True, unique=True) #steam_appid

    #name
    name = models.CharField(max_length=100, default="game")

    #short_description, detailed_description, about_the_game
    description = models.TextField(default="description")

    #release_date
    release_date = models.DateField(default=timezone.now) 

    #developers
    developer = models.JSONField(default=dict)

    #publishers
    publisher = models.JSONField(default=dict)

    #categories
    categories = models.JSONField(default=dict)

    #Background_raw, header_image
    header_image = models.URLField(default="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png") 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'pk': self.pk})
