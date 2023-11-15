from django.db import models


class AdvancedStatistics(models.Model):
    valorization = models.FloatField()
    effectiveFieldGoalPercentage = models.FloatField()
    trueShootingPercentage = models.FloatField()
    hollingerAssistRatio = models.FloatField()

    def save(self, *args, **kwargs):
        for k, v in self.__dict__.items():
            if k in ('valorization', 'effectiveFieldGoalPercentage', 'trueShootingPercentage', 'hollingerAssistRatio'):
                setattr(self, k, round(v, 1))
        super(AdvancedStatistics, self).save(*args, **kwargs)
