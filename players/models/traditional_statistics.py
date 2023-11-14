from django.db import models
from .shot_statistics import ShotStatistics


class TraditionalStatistics(models.Model):
    freeThrows = models.OneToOneField(ShotStatistics, related_name='free_throws', on_delete=models.CASCADE)
    twoPoints = models.OneToOneField(ShotStatistics, related_name='two_points', on_delete=models.CASCADE)
    threePoints = models.OneToOneField(ShotStatistics, related_name='three_points', on_delete=models.CASCADE)
    points = models.FloatField()
    rebounds = models.FloatField()
    blocks = models.FloatField()
    assists = models.FloatField()
    steals = models.FloatField()
    turnovers = models.FloatField()

    def save(self, *args, **kwargs):
        self.points = round(self.points, 1)
        self.rebounds = round(self.rebounds, 1)
        self.blocks = round(self.blocks, 1)
        self.assists = round(self.assists, 1)
        self.steals = round(self.steals, 1)
        self.turnovers = round(self.turnovers, 1)
        super(TraditionalStatistics, self).save(*args, **kwargs)
