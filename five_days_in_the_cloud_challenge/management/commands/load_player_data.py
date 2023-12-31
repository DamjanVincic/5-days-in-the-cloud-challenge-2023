from django.core.management.base import BaseCommand
from five_days_in_the_cloud_challenge.utils import load_player_data

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        load_player_data()
