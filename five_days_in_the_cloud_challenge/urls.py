from django.urls import path, include
from players.urls import urlpatterns as player_urlpatterns

urlpatterns = [
    path('stats/player/', include(player_urlpatterns))
]
