from django.core.management.base import BaseCommand
from data_collectors.reviews_collector import initial_reviews_collector

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        initial_reviews_collector(options["id"])
