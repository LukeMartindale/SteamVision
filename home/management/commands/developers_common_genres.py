from django.core.management.base import BaseCommand
from data_processors.app_developers import developer_common_genres_find_all

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--id")

    def handle(self, *args, **options):
        developer_common_genres_find_all()