from rest_framework import serializers
from players.models import ShotStatistics


class ShotStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShotStatistics
        fields = "__all__"