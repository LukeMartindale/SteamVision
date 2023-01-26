from django.core.management.base import BaseCommand
from data_processors.app_emotions import app_all_emotions

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        app_all_emotions()
