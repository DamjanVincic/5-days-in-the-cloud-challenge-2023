from django.core.management.base import BaseCommand
from players.models import Player, PlayerStatistics
from players.serializers import PlayerStatisticsSerializer

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if PlayerStatistics.objects.exists():
            self.stdout.write(self.style.WARNING('Statistics already exists.'))
            return

        players = Player.objects.all()

        for player in players:
            data = {
                "playerName": player.player,
                "gamesPlayed": player.gamesPlayed,
                "traditional": {
                    "freeThrows": {
                        "attempts": player.FTA,
                        "made": player.FTM,
                        "shootingPercentage": 0 if not player.FTA else player.FTM/player.FTA*100
                    },
                    "twoPoints": {
                        "attempts": player.TWO_PA,
                        "made": player.TWO_PM,
                        "shootingPercentage": 0 if not player.TWO_PA else player.TWO_PM/player.TWO_PA*100
                    },
                    "threePoints": {
                        "attempts": player.THREE_PA,
                        "made": player.THREE_PM,
                        "shootingPercentage": 0 if not player.THREE_PA else player.THREE_PM/player.THREE_PA*100
                    },
                    "points": player.FTM + player.TWO_PM*2 + player.THREE_PM*3,
                    "rebounds": player.REB,
                    "blocks": player.BLK,
                    "assists": player.AST,
                    "steals": player.STL,
                    "turnovers": player.TOV,
                },
                "advanced": {
                    "valorization": (player.FTM + 2*player.TWO_PM + 3* player.THREE_PM + player.REB + player.BLK + player.AST + player.STL - (player.FTA - player.FTM + player.TWO_PA - player.TWO_PM + player.THREE_PA - player.THREE_PM + player.TOV))/player.gamesPlayed,
                    "effectiveFieldGoalPercentage": 0 if (player.TWO_PA + player.THREE_PA) == 0 else (player.TWO_PM + player.THREE_PM + 0.5*player.THREE_PM) / (player.TWO_PA + player.THREE_PA) * 100,
                    "trueShootingPercentage": 0 if (2*(player.TWO_PA + player.THREE_PA + 0.475*player.FTA)) == 0 else (player.FTM + player.TWO_PM*2 + player.THREE_PM*3) / (2*(player.TWO_PA + player.THREE_PA + 0.475*player.FTA)) * 100,
                    "hollingerAssistRatio": 0 if (player.TWO_PA + player.THREE_PA + 0.475*player.FTA + player.AST + player.TOV) == 0 else player.AST / (player.TWO_PA + player.THREE_PA + 0.475*player.FTA + player.AST + player.TOV) * 100
                }
            }
            
            # Dividing by games played
            for k, v in data.items():
                if k == "traditional":
                    for k2, v2 in v.items():
                        if isinstance(v2, dict):
                            v2["attempts"] /= player.gamesPlayed
                            v2["made"] /= player.gamesPlayed
                        else:
                            v[k2] /= player.gamesPlayed

            serializer = PlayerStatisticsSerializer(data=data)
            if (serializer.is_valid()):
                serializer.save()
            else:
                self.stderr.write(self.style.ERROR(serializer.errors))

        self.stdout.write(self.style.SUCCESS('Calculated statistics successfully'))