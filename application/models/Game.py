""" application/models/Game.py
"""

from Player import Player


class Game(object):
    """Game object for taking care of global game data"""
    def __init__(self):
        self.playerlist = {}
        # self.userlist = {}

    def addplayer(self, username):
        """Adds new player to game"""
        # if not self.userexists(username):
        #     raise KeyError('User not yet added to userlist')
        if self.userisplaying(username):
            raise ValueError('User is already online')

        player = Player(self, username)
        self.playerlist[player.username] = player

    def removeplayer(self, username):
        """Removes player from game"""
        if not self.userisplaying(username):
            return False

        self.playerlist.pop(username)
        return True

    # def userexists(self, username):
    #     """Returns true if username is part of list"""
    #     return username in self.userlist

    def userisplaying(self, username):
        """Returns true if player is online"""
        return username in self.playerlist
