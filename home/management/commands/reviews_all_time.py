from django.core.management.base import BaseCommand
from data_processors.reviews import reviews_all_time_year, reviews_all_time_year_all, reviews_all_time_year_legacy, reviews_all_time_year_legacy_all

class Command(BaseCommand):

    help = "Gets the data about a game on Steam. You must provide the games steam id as an --id argument for the command"

    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--legacy")

    def handle(self, *args, **options):
        if(options["legacy"] == "true"):
            if(options["id"].lower() == "all"):
                reviews_all_time_year_legacy_all()
            else:
                reviews_all_time_year_legacy(options["id"])
        else:
            if(options["id"].lower() == "all"):
                reviews_all_time_year_all()
            else:
                reviews_all_time_year(options["id"])
