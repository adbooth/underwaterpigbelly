""" application/models/Game.py
"""

from flask import json

from Player import Player


class Game(object):
    """Game object for taking care of global game data"""
    def __init__(self):
        self.playerlist = {}

    def add(self, obj):
        """Adds element to game"""
        if type(obj).__name__ == 'Player':
            if self.userisplaying(obj.username):
                raise ValueError('User is already online')
            self.playerlist[obj.username] = obj
        else:
            raise TypeError('Objects of type ' + type(obj).__name__ + 'are not supported by the game object')

    def addplayer(self, username, x=50, y=50):
        """Adds player to playerlist"""
        player = Player(self, username, x, y)
        self.add(player)

    def userisplaying(self, username):
        """Returns true if player is online"""
        return username in self.playerlist

    def getplayer(self, username):
        """Returns player given username"""
        if self.userisplaying(username):
            return self.playerlist[username]
        return False

    def updateplayer(self, username, x, y):
        """
        I really shouldn't have to describe a method who's
        name implies its function as obviously as this one
        """
        player = self.getplayer(username)
        player.x = x
        player.y = y

    def remove(self, obj):
        """Removes element from game"""
        if type(obj).__name__ == 'Player':
            if not self.userisplaying(obj.username):
                raise KeyError('Username does not belong to online user')
            self.playerlist.pop(obj.username)
        else:
            raise TypeError('Objects of type ' + type(obj).__name__ + 'are not supported by the game object')

    def removeplayer(self, username):
        """Removes player from playerlist"""
        return self.remove(self.getplayer(username))

    def dumps(self):
        """Returns game object as JSONified string"""
        data = {}
        data['playerlist'] = {username: player.dumps() for username, player in self.playerlist.iteritems()}
        return json.dumps(data)
