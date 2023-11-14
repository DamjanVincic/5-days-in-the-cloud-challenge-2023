from django.db import models


class AdvancedStatistics(models.Model):
    valorization = models.FloatField()
    effectiveFieldGoalPercentage = models.FloatField()
    trueShootingPercentage = models.FloatField()
    hollingerAssistRatio = models.FloatField()

    def save(self, *args, **kwargs):
        self.valorization = round(self.valorization, 1)
        self.effectiveFieldGoalPercentage = round(self.effectiveFieldGoalPercentage, 1)
        self.trueShootingPercentage = round(self.trueShootingPercentage, 1)
        self.hollingerAssistRatio = round(self.hollingerAssistRatio, 1)
        super(AdvancedStatistics, self).save(*args, **kwargs)
