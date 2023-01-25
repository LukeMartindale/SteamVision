from django.core.management.base import BaseCommand
from data_collectors.player_count_collector import player_count_all_collector

class Command(BaseCommand):

    help = "Gets the current player count for all games in the database. Intended to be run on the heroku scheduler"

    def handle(self, *args, **options):
        player_count_all_collector()
        print("getAllPlayers Finished")
