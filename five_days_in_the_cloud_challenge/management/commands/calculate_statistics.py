from django.core.management.base import BaseCommand
from players.models import Player, PlayerStatistics
from players.serializers import PlayerStatisticsSerializer
from five_days_in_the_cloud_challenge.utils import calculate_statistics

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        calculate_statistics()
