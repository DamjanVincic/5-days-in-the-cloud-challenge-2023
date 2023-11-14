from rest_framework import serializers
from players.models import AdvancedStatistics


class AdvancedStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedStatistics
        fields = "__all__"