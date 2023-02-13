from django.core.management.base import BaseCommand
from data_processors.app_sentiment import calc_sentiment_score

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        calc_sentiment_score(options["id"])