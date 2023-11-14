from rest_framework import serializers
from players.models import Player


class PlayerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
