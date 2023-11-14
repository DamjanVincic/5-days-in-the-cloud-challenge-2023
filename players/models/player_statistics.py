from django.db import models
from .traditional_statistics import TraditionalStatistics
from .advanced_statistics import AdvancedStatistics


class PlayerStatistics(models.Model):
    playerName = models.CharField(max_length=50)
    gamesPlayed = models.IntegerField()
    traditional = models.OneToOneField(TraditionalStatistics, on_delete=models.CASCADE)
    advanced = models.OneToOneField(AdvancedStatistics, on_delete=models.CASCADE)
