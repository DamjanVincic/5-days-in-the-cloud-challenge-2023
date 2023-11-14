from django.db import models


class AdvancedStatistics(models.Model):
    valorization = models.FloatField()
    effectiveFieldGoalPercentage = models.FloatField()
    trueShootingPercentage = models.FloatField()
    hollingerAssistRatio = models.FloatField()
