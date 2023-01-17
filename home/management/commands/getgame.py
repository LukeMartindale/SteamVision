from django.core.management.base import BaseCommand
from data_collectors.game_collector import game_collector

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        game_collector(options["id"])
