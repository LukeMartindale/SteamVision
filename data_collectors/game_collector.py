from data_collectors.collector_helpers import convertDate, descriptionStripper, tagStripper, newDescriptors

from home.models import Game
import requests
from bs4 import BeautifulSoup

def game_collector(game_id):
    api_url = "http://store.steampowered.com/api/appdetails?appids={}&cc=UK".format(game_id)
    response_app = requests.get(api_url).json()

    tag_url = "https://store.steampowered.com/apphoverpublic/{}".format(game_id)
    response_tags = requests.get(tag_url)

    tags = tagStripper(response_tags)

    newDescriptors(descriptionStripper(response_app[game_id]["data"]["genres"]), tags, descriptionStripper(response_app[game_id]["data"]["categories"]))

    if(Game.objects.filter(app_id=game_id).exists()):
        game = Game.objects.get(app_id=game_id)
    else:
        game = Game()



    game.app_id = response_app[game_id]["data"]["steam_appid"]
    game.name = response_app[game_id]["data"]["name"]
    game.description = response_app[game_id]["data"]["short_description"]

    game.release_date = convertDate(response_app[game_id]["data"]["release_date"]["date"])
    game.developer = response_app[game_id]["data"]["developers"]
    game.publisher = response_app[game_id]["data"]["publishers"]

    game.genres =  descriptionStripper(response_app[game_id]["data"]["genres"])
    game.tags = tags
    game.categories = descriptionStripper(response_app[game_id]["data"]["categories"])
    game.supported_languages = response_app[game_id]["data"]["supported_languages"]

    game.header_image = response_app[game_id]["data"]["header_image"]

    game.save()