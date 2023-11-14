from django.db import models


class ShotStatistics(models.Model):
    attempts = models.FloatField()
    made = models.FloatField()
    shootingPercentage = models.FloatField()