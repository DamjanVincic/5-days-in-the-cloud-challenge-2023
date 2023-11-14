from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerialzer
from .models import ShotStatistics, PlayerStatistics
from .serializers import ShotStatisticsSerializer, PlayerStatisticsSerializer


class PlayerListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        serializer = PlayerSerialzer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PlayerStatisticsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        player_statistics = PlayerStatistics.objects.all()
        serializer = PlayerStatisticsSerializer(player_statistics, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class PlayerStatisticsDetailsAPIView(APIView):
    def get(self, request, playerFullName, *args, **kwargs):
        try:
            player_statistics = PlayerStatistics.objects.get(playerName=playerFullName)
            serializer = PlayerStatisticsSerializer(player_statistics)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except PlayerStatistics.DoesNotExist:
            return Response(data={"explanation": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
