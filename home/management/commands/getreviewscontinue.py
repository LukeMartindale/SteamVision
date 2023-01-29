from django.core.management.base import BaseCommand
from data_collectors.reviews_collector import initial_reviews_collector_continue

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--cursor")

    def handle(self, *args, **options):
        if(options["id"]):
            initial_reviews_collector_continue(options["id"], options["cursor"])
        else:
            print("Please Provide a game ID")