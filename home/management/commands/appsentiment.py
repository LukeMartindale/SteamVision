from django.core.management.base import BaseCommand
from data_processors.app_sentiment import app_sentiment

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        sentiment = app_sentiment(options["id"])