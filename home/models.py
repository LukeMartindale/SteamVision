from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Game(models.Model):
    #steam_appid
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
    #genres
    genres = models.JSONField(default=dict)
    #categories
    categories = models.JSONField(default=dict)
    #supported_languages
    supported_languages = models.TextField(default="Languages")
    #Background_raw, header_image
    header_image = models.URLField(default="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'pk': self.pk})

class Review(models.Model):

    #what app this review belongs to
    app_id = models.ForeignKey(Game, on_delete=models.CASCADE, default=0)
    #recommendationid
    review_id = models.IntegerField(default=0)
    #author
    author_id = models.IntegerField(default=0)
    #language
    language = models.CharField(max_length=50, default="")
    #review
    review_text = models.TextField(default="")
    #timestamp_created
    time_created = models.DateField(default=timezone.now)
    #playtime_at_review(In Minutes)
    playtime_at_review = models.IntegerField(default=-1)
    #voted_up
    voted_up = models.BooleanField(default=False)
    #votes_up
    votes_up = models.IntegerField(default=0)
    #votes_funny
    votes_funny = models.IntegerField(default=0)
    #steam_purchase
    purchase_on_steam = models.BooleanField(default=True)
    #received_for_free
    received_for_free = models.BooleanField(default=False)
    #written_during_early_access
    written_during_early_access = models.BooleanField(default=False)

    def __str__(self):
        return "{app_name}/{review_id}".format(app_name=self.app_id.name, review_id = str(self.review_id))

    def get_absolute_url(self):
        return reverse('review', kwargs={'pk': self.pk})
