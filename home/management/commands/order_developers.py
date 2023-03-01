from django.core.management.base import BaseCommand
from data_processors.app_developers import order_developer_games, order_developer_games_all

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        if(options["id"].lower() == "all"):
            order_developer_games_all()
        else:
            order_developer_games(options["id"])