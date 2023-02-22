from django.core.management.base import BaseCommand
from data_processors.reviews import (
    reviews_past_month,
    reviews_past_month_all,
    )

class Command(BaseCommand):

    help = "Gets the data about a game on Steam. You must provide the games steam id as an --id argument for the command"

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        if(options["id"].lower() == "all"):
            reviews_past_month_all()
        else:
            reviews_past_month(options["id"])
