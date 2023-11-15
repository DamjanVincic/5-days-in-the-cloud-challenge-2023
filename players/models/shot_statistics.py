from django.db import models


class ShotStatistics(models.Model):
    attempts = models.FloatField()
    made = models.FloatField()
    shootingPercentage = models.FloatField()

    def save(self, *args, **kwargs):
        for k, v in self.__dict__.items():
            if k in ('attempts', 'made', 'shootingPercentage'):
                setattr(self, k, round(v, 1))
        super(ShotStatistics, self).save(*args, **kwargs)