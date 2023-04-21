from django.core.management.base import BaseCommand
from data_processors.reviews import format_current_reviews_text

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        format_current_reviews_text()