from django.core.management.base import BaseCommand
from data_processors.app_sentiment import (
    app_sentiment_all_time_month, 
    app_sentiment_all_time_month_all, 
    app_sentiment_past_one_month, 
    app_sentiment_past_one_month_all,
    app_sentiment_past_two_weeks,
    app_sentiment_past_two_weeks_all,
    app_sentiment_past_one_week,
    app_sentiment_past_one_week_all)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--time")

    def handle(self, *args, **options):
        if options["time"].lower() == "all-time" or None:
            if(options["id"].lower() == "all"):
                app_sentiment_all_time_month_all()
            else:
                app_sentiment_all_time_month(options["id"])
        elif options["time"].lower() == "one-month":
            if(options["id"].lower() == "all"):
                app_sentiment_past_one_month_all()
            else:
                app_sentiment_past_one_month(options["id"])
        elif options["time"].lower() == "two-weeks":
            if(options["id"].lower() == "all"):
                app_sentiment_past_two_weeks_all()
            else:
                app_sentiment_past_two_weeks(options["id"])
        elif options["time"].lower() == "one-week":
            if(options["id"].lower() == "all"):
                app_sentiment_past_one_week_all()
            else:
                app_sentiment_past_one_week(options["id"])
