from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    #user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    #followed_games
    followed_games = models.JSONField(default=dict)

    #system_info
    system_info = models.JSONField(default=dict)
