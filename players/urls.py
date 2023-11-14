from django.urls import path
from .views import PlayerStatisticsDetailsAPIView


urlpatterns = [
    path('<str:playerFullName>/', PlayerStatisticsDetailsAPIView.as_view()),
]
