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
        for k, v in self.__dict__.items():
            if k in ('points', 'rebounds', 'blocks', 'assists', 'steals', 'turnovers'):
                setattr(self, k, round(v, 1))
        super(TraditionalStatistics, self).save(*args, **kwargs)
