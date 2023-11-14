from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlayerStatistics
from .serializers import PlayerStatisticsSerializer

    
class PlayerStatisticsDetailsAPIView(APIView):
    def get(self, request, playerFullName, *args, **kwargs):
        try:
            player_statistics = PlayerStatistics.objects.get(playerName=playerFullName)
            serializer = PlayerStatisticsSerializer(player_statistics)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except PlayerStatistics.DoesNotExist:
            return Response(data={"explanation": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
