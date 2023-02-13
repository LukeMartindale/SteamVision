from data_collectors.collector_helpers import convertDate, descriptionStripper, tagStripper, newDescriptors

from home.models import Game
import requests
from bs4 import BeautifulSoup

def game_collector(game_id):
    api_url = "http://store.steampowered.com/api/appdetails?appids={}&cc=UK".format(game_id)
    response_app = requests.get(api_url).json()

    # print(response_app[game_id]["data"]["pc_requirements"])
    # print(response_app[game_id]["data"]["mac_requirements"])
    # print(response_app[game_id]["data"]["linux_requirements"])

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

def game_recollector():

    games = Game.objects.all()

    for g in games:

        print(g)

        game_id = str(g.app_id)

        api_url = "http://store.steampowered.com/api/appdetails?appids={}&cc=UK".format(game_id)
        response_app = requests.get(api_url).json()

        # if response_app[game_id]["data"]["pc_requirements"]: 
        #     print(response_app[game_id]["data"]["pc_requirements"])
        # else:
        #     print("pc_requirements none")

        # if response_app[game_id]["data"]["mac_requirements"]:
        #     print(response_app[game_id]["data"]["mac_requirements"])
        # else:
        #     print("mac_requirements none")

        # if response_app[game_id]["data"]["linux_requirements"]:
        #     print(response_app[game_id]["data"]["linux_requirements"])
        # else:
        #     print("linux_requirements none")

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

        game.windows_support = response_app[game_id]["data"]["platforms"]["windows"]
        game.mac_support = response_app[game_id]["data"]["platforms"]["mac"]
        game.linux_support = response_app[game_id]["data"]["platforms"]["linux"]

        game.genres =  descriptionStripper(response_app[game_id]["data"]["genres"])
        game.tags = tags
        game.categories = descriptionStripper(response_app[game_id]["data"]["categories"])
        game.supported_languages = response_app[game_id]["data"]["supported_languages"]

        game.header_image = response_app[game_id]["data"]["header_image"]

        game.save()
