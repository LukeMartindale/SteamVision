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

    #price
    price = models.IntegerField(default=0)

    #release_date
    release_date = models.DateField(default=timezone.now) 
    #developers
    developer = models.JSONField(default=dict)
    #publishers
    publisher = models.JSONField(default=dict)

    #genres
    genres = models.JSONField(default=dict)
    #tags
    tags = models.JSONField(default=dict)
    #categories
    categories = models.JSONField(default=dict)

    #windows_support
    windows_support = models.BooleanField(default=False)
    #windows_requirements
    windows_requirements = models.JSONField(default=dict)
    #mac_support
    mac_support = models.BooleanField(default=False)
    #mac_requirements
    mac_requirements = models.JSONField(default=dict)
    #linux_support
    linux_support = models.BooleanField(default=False)
    #linux_requirements
    linux_requirements = models.JSONField(default=dict)

    #supported_languages
    supported_languages = models.TextField(default="Languages")

    #Background_raw, header_image
    header_image = models.URLField(default="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'pk': self.pk})

class GameStat(models.Model):

    #app
    app_id = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

    #sentiment
    sentiment = models.JSONField(default=dict)

    #emotion
    emotion = models.JSONField(default=dict)

    #highest_player_count
    highest_player_count = models.IntegerField(default=0)

    #highest_player_count_date
    highest_player_count_date = models.DateField(default=timezone.now)

    #highest_review_score
    highest_review_score = models.IntegerField(default=0)

    #highest_sentiment_score
    highest_sentiment_score = models.FloatField(default=0.0)

    #highest_sentiment_score_date
    highest_sentiment_score_date = models.DateField(default=timezone.now)

    #current_sentiment_score
    current_sentiment_score = models.FloatField(default=0.0)

    def __str__(self):
        return "{} Stats".format(self.app_id.name)

    def get_absolute_url(self):
        return reverse('gamestat', kwargs={'pk': self.pk})

class PlayerCount(models.Model):
    #app
    app_id = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    #Player Count
    player_count = models.IntegerField(default=-1)
    #TimeStamp
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}/{}/{} - {} - {}".format(self.timestamp.day, self.timestamp.month, self.timestamp.year ,self.timestamp.hour, self.app_id)

    def get_absolute_url(self):
        return reverse('playercount', kwargs={'pk': self.pk})


class Review(models.Model):

    #app, recommendationid, author
    app_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_id = models.BigIntegerField(default=0)
    author_id = models.BigIntegerField(default=0)

    #language, review
    language = models.CharField(max_length=50, default="")
    review_text = models.TextField(default="")

    #sentiment_pos, sentiment_polarity, sentiment_subjectivity
    sentiment_pos = models.BooleanField(default=True)
    sentiment_polarity = models.FloatField(default=0)
    sentiment_subjectivity = models.FloatField(default=0)

    #emotion_scores, emotions_prominent
    emotion_scores = models.JSONField(default=dict)
    emotion_prominent = models.JSONField(default=dict)

    #timestamp_created, playtime_at_review(In Minutes)
    time_created = models.DateField(default=timezone.now)
    playtime_at_review = models.BigIntegerField(default=-1)

    #voted_up, votes_up, votes_funny
    voted_up = models.BooleanField(default=False)
    votes_up = models.IntegerField(default=0)
    votes_funny = models.BigIntegerField(default=0)

    #steam_purchase, received_for_free, written_during_early_access
    purchase_on_steam = models.BooleanField(default=True)
    received_for_free = models.BooleanField(default=False)
    written_during_early_access = models.BooleanField(default=False)

    def __str__(self):
        return "{app_name}/{review_id}".format(app_name=self.app_id.name, review_id = str(self.review_id))

    def get_absolute_url(self):
        return reverse('review', kwargs={'pk': self.pk})

class Descriptor(models.Model):

    type = models.CharField(max_length=20, default="")

    name = models.CharField(max_length=100, default="")

    symbol = models.CharField(max_length=100, default="bi-asterisk")

    def __str__(self):
        return "{descriptor_type} - {descriptor_name}".format(descriptor_type=self.type, descriptor_name=self.name)

    def get_absolute_url(self):
        return reverse('descriptor', kwargs={'pk': self.pk})

class Developer(models.Model):

    name = models.CharField(max_length=100, default="")
