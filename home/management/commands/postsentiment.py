from django.core.management.base import BaseCommand
from data_processors.post_sentiment import post_sentiment

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        post_sentiment(options["id"])