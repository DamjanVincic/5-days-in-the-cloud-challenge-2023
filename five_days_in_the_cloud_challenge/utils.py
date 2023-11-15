import csv
from players.models import Player, PlayerStatistics
from players.serializers import PlayerSerialzer, PlayerStatisticsSerializer


def load_player_data():
    if Player.objects.exists():
        print('Data already exists.')
    else:
        with open('L9HomeworkChallengePlayersInput.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data = {
                    'player': row['\ufeffPLAYER'], # It reads a character before the word
                    'position': row['POSITION'],
                    'FTM': row['FTM'],
                    'FTA': row['FTA'],
                    'TWO_PM': row['2PM'],
                    'TWO_PA': row['2PA'],
                    'THREE_PM': row['3PM'],
                    'THREE_PA': row['3PA'],
                    'REB': row['REB'],
                    'BLK': row['BLK'],
                    'AST': row['AST'],
                    'STL': row['STL'],
                    'TOV': row['TOV']
                }
                
                try:
                    player = Player.objects.get(player=data['player'])
                    for k, v in data.items():
                        if k not in ('player, position'):
                            setattr(player, k, getattr(player, k) + int(v))
                    player.gamesPlayed += 1
                    player.save()
                except Player.DoesNotExist:
                    serializer = PlayerSerialzer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)

        print('Data loaded successfully')


def calculate_statistics():
    if PlayerStatistics.objects.exists():
        print('Statistics already exists.')
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
            print(serializer.errors)

    print('Calculated statistics successfully')