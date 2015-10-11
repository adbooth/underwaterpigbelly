""" application/models/Game.py
"""

from Player import Player


class Game(object):
    """Game object for taking care of global game data"""
    def __init__(self):
        self.playerlist = {}

    def addplayer(self, username):
        """Adds new player to game"""
        if username in self.playerlist:
            return False

        player = Player(self, username)
        self.playerlist[player.username] = player
        return True

    def removeplayer(self, username):
        """Removes player from game"""
        if username in self.playerlist:
            del self.playerlist[username]
            return True
        return False
