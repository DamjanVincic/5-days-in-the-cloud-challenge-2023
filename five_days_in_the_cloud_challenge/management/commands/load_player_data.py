import csv
from django.core.management.base import BaseCommand
from players.models import Player
from players.serializers import PlayerSerialzer

class Command(BaseCommand):
    help = 'Loads data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        if Player.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists.'))
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
                            self.stderr.write(self.style.ERROR(serializer.errors))

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))