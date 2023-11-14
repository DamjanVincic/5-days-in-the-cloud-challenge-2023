from django.contrib import admin
from django.urls import path, include
from players.urls import urlpatterns as player_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/player/', include(player_urlpatterns))
]
