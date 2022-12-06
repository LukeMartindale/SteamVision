from home.models import Game
from helper_files.datetimeFormater import convertDate
import requests


def getGame(game_id):

    api_url = "http://store.steampowered.com/api/appdetails?appids={}&cc=UK".format(game_id)
    response_app = requests.get(api_url).json()

    game = Game()

    game.app_id = response_app[game_id]["data"]["steam_appid"]
    game.name = response_app[game_id]["data"]["name"]
    game.description = response_app[game_id]["data"]["short_description"]

    game.release_date = convertDate(response_app[game_id]["data"]["release_date"]["date"])
    game.developer = response_app[game_id]["data"]["developers"]
    game.publisher = response_app[game_id]["data"]["publishers"]

    game.categories = response_app[game_id]["data"]["categories"]
    game.supported_languages = response_app[game_id]["data"]["supported_languages"]

    game.header_image = response_app[game_id]["data"]["header_image"]

    game.save()
