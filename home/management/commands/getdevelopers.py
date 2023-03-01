from django.core.management.base import BaseCommand
from data_processors.app_developers import get_developers, get_developers_all

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        if(options["id"].lower() == "all"):
            get_developers_all()
        else:
            get_developers(options["id"])
