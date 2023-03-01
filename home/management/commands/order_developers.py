from django.core.management.base import BaseCommand
from data_processors.app_developers import order_developer_games_all

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        order_developer_games_all()
