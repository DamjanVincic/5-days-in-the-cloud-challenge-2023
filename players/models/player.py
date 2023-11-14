from django.db import models
from enum import Enum


class Positions(Enum):
    PG = 'PG'
    SG = 'SG'
    SF = 'SF'
    PF = 'PF'
    C = 'C'

class Player(models.Model):
    player = models.CharField(max_length=50) # Player's full name
    position = models.CharField(max_length=2, choices=[(position.name, position.value) for position in Positions])
    FTM = models.IntegerField() # Free Throws Made
    FTA = models.IntegerField() # Free Throws Attempted
    TWO_PM = models.IntegerField() # Two Points Made
    TWO_PA = models.IntegerField() # Two Points Attempted
    THREE_PM = models.IntegerField() # Three Points Made
    THREE_PA = models.IntegerField() # Three Points Attempted
    REB = models.IntegerField() # Rebounds
    BLK = models.IntegerField() # Blocks
    AST = models.IntegerField() # Assists
    STL = models.IntegerField() # Steals
    TOV = models.IntegerField() # Turnovers
    gamesPlayed = models.IntegerField(default=1)
