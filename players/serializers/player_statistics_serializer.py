from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from players.models import PlayerStatistics, TraditionalStatistics, AdvancedStatistics, ShotStatistics
from . import TraditionalStatisticsSerializer, AdvancedStatisticsSerializer, ShotStatisticsSerializer

class PlayerStatisticsSerializer(WritableNestedModelSerializer):
    traditional = TraditionalStatisticsSerializer()
    advanced = AdvancedStatisticsSerializer()

    class Meta:
        model = PlayerStatistics
        exclude = ('id',)
