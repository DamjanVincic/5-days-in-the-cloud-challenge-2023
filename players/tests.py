from django.test import TestCase
from five_days_in_the_cloud_challenge.utils import load_player_data, calculate_statistics
from players.models import Player


class PlayerTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        load_player_data()
        calculate_statistics()

    def test_save_players(self):
        try:
            player = Player.objects.get(player="Jaysee Nkrumah")
            self.assertEqual(player.player, "Jaysee Nkrumah")
        except Player.DoesNotExist:
            self.fail("Player not found")

    def test_check_statistics(self):
        response = self.client.get('/stats/player/Sifiso Abdalla/')
        self.assertNotEqual(response.status_code, 404)

        data = {
            "playerName": "Sifiso Abdalla",
            "gamesPlayed": 3,
            "traditional": {
                "freeThrows": {
                    "attempts": 4.7,
                    "made": 3.3,
                    "shootingPercentage": 71.4
                },
                "twoPoints": {
                    "attempts": 4.7,
                    "made": 3.0,
                    "shootingPercentage": 64.3
                },
                "threePoints": {
                    "attempts": 6.3,
                    "made": 1.0,
                    "shootingPercentage": 15.8
                },
                "points": 12.3,
                "rebounds": 5.7,
                "blocks": 1.7,
                "assists": 0.7,
                "steals": 1.0,
                "turnovers": 1.3
            },
            "advanced": {
                "valorization": 11.7,
                "effectiveFieldGoalPercentage": 40.9,
                "trueShootingPercentage": 46.7,
                "hollingerAssistRatio": 4.4
            }
        }
        self.assertEqual(response.data, data)
