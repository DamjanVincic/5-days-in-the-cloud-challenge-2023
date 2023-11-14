from django.urls import path, include
from .views import PlayerListAPIView


urlpatterns = [
    path('', PlayerListAPIView.as_view())
]
