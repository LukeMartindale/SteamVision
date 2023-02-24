from django.core.management.base import BaseCommand
from data_processors.app_sentiment import app_sentiment_all_time_month, app_sentiment_all_time_month_all

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        if(options["id"].lower() == "all"):
            app_sentiment_all_time_month_all()
        else:
            app_sentiment_all_time_month(options["id"])