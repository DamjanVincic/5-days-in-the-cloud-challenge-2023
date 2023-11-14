from django.db import models


class ShotStatistics(models.Model):
    attempts = models.FloatField()
    made = models.FloatField()
    shootingPercentage = models.FloatField()

    def save(self, *args, **kwargs):
        self.attempts = round(self.attempts, 1)
        self.made = round(self.made, 1)
        self.shootingPercentage = round(self.shootingPercentage, 1)
        super(ShotStatistics, self).save(*args, **kwargs)