from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerialzer


class PlayerListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        serializer = PlayerSerialzer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
