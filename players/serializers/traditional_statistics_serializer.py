from rest_framework import serializers
from players.models import TraditionalStatistics
from . import ShotStatisticsSerializer


class TraditionalStatisticsSerializer(serializers.ModelSerializer):
    freeThrows = ShotStatisticsSerializer()
    twoPoints = ShotStatisticsSerializer()
    threePoints = ShotStatisticsSerializer()

    class Meta:
        model = TraditionalStatistics
        fields = "__all__"