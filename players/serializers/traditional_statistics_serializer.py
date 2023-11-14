from drf_writable_nested.serializers import WritableNestedModelSerializer
from players.models import TraditionalStatistics
from . import ShotStatisticsSerializer


class TraditionalStatisticsSerializer(WritableNestedModelSerializer):
    freeThrows = ShotStatisticsSerializer()
    twoPoints = ShotStatisticsSerializer()
    threePoints = ShotStatisticsSerializer()

    class Meta:
        model = TraditionalStatistics
        exclude = ('id',)