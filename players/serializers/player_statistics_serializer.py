from rest_framework import serializers
from players.models import PlayerStatistics
from . import TraditionalStatisticsSerializer, AdvancedStatisticsSerializer

class PlayerStatisticsSerializer(serializers.ModelSerializer):
    traditional = TraditionalStatisticsSerializer()
    advanced = AdvancedStatisticsSerializer()

    class Meta:
        model = PlayerStatistics
        fields = "__all__"