from drf_writable_nested.serializers import WritableNestedModelSerializer
from players.models import PlayerStatistics
from . import TraditionalStatisticsSerializer, AdvancedStatisticsSerializer

class PlayerStatisticsSerializer(WritableNestedModelSerializer):
    traditional = TraditionalStatisticsSerializer()
    advanced = AdvancedStatisticsSerializer()

    class Meta:
        model = PlayerStatistics
        exclude = ('id',)
