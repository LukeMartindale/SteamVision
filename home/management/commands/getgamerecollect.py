from django.core.management.base import BaseCommand
from data_collectors.game_collector import game_recollector

class Command(BaseCommand):

    help = "Gets the data about a game on Steam. You must provide the games steam id as an --id argument for the command"

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        game_recollector()