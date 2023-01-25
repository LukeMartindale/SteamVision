from django.core.management.base import BaseCommand
from data_collectors.reviews_collector import reviews_new_all_collector

class Command(BaseCommand):

    help = "Get the new reviews for all games stored in the database"

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        if(options["id"]):
            print("reviews_new_collector")
            print("Not Yet Implemented")
        else:
            reviews_new_all_collector()
