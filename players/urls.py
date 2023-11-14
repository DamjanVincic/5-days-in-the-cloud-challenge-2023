from django.urls import path, include
from .views import PlayerListAPIView
from .views import PlayerStatisticsListAPIView, PlayerStatisticsDetailsAPIView


urlpatterns = [
    path('', PlayerStatisticsListAPIView.as_view()),
    path('<str:playerFullName>/', PlayerStatisticsDetailsAPIView.as_view()),
]
