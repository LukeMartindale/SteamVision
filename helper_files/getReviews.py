from home.models import Review
from datetime import datetime
from home.models import Game, Review

def getReviews(game_id):

    api_url = "https://store.steampowered.com/appreviews/{}?json=1".format(game_id)

    timestamp = 1669384225
    dt = datetime.fromtimestamp(timestamp)

# def getReviewsStats(game_id):

#     game = Game.objects.filter(pk=game_id)

#     print(game[0])

#     rvstat = ReviewsStat()

#     rvstat.app = game.first()
#     rvstat.review_data_id = game_id
#     rvstat.sentiment = [
#         {'label': '-1', 'value': 2}, 
#         {'label': '-0.9', 'value': 3}, 
#         {'label': '-0.8', 'value': 1}, 
#         {'label': '-0.7', 'value': 3}, 
#         {'label': '-0.6', 'value': 5}, 
#         {'label': '-0.5', 'value': 14}, 
#         {'label': '-0.4', 'value': 59}, 
#         {'label': '-0.3', 'value': 9}, 
#         {'label': '-0.2', 'value': 41}, 
#         {'label': '-0.1', 'value': 55}, 
#         {'label': '0', 'value': 539}, 
#         {'label': '0.1', 'value': 199}, 
#         {'label': '0.2', 'value': 141}, 
#         {'label': '0.3', 'value': 178}, 
#         {'label': '0.4', 'value': 47}, 
#         {'label': '0.5', 'value': 99}, 
#         {'label': '0.6', 'value': 47}, 
#         {'label': '0.7', 'value': 60}, 
#         {'label': '0.8', 'value': 21}, 
#         {'label': '0.9', 'value': 13}, 
#         {'label': '1', 'value': 64},
#     ]

#     rvstat.save()
