""" application/models/Game.py
"""

from flask import json

from Player import Player


class Game(object):
    """Game object for taking care of global game data"""
    def __init__(self):
        self.players = {}

    def add(self, obj):
        """Adds element to game"""
        if type(obj).__name__ == 'Player':
            if self.userIsPlaying(obj.username):
                raise ValueError('User is already online')
            self.players[obj.username] = obj
        else:
            raise TypeError('Objects of type ' + type(obj).__name__ + 'are not supported by the game object')

    def addPlayer(self, username, x=50, y=50):
        """Adds player to players"""
        player = Player(self, username, x, y)
        self.add(player)

    def userIsPlaying(self, username):
        """Returns true if player is online"""
        return username in self.players

    def getPlayer(self, username):
        """Returns player given username"""
        if self.userIsPlaying(username):
            return self.players[username]
        return False

    def updatePlayer(self, username, x, y):
        """
        I really shouldn't have to describe a method who's
        name implies its function as obviously as this one
        """
        player = self.getPlayer(username)
        player.x = x
        player.y = y

    def remove(self, obj):
        """Removes element from game"""
        if type(obj).__name__ == 'Player':
            if not self.userIsPlaying(obj.username):
                raise KeyError('Username does not belong to online user')
            self.players.pop(obj.username)
        else:
            raise TypeError('Objects of type ' + type(obj).__name__ + 'are not supported by the game object')

    def removePlayer(self, username):
        """Removes player from players"""
        return self.remove(self.getPlayer(username))

    def dumps(self):
        """Returns game object as JSONified string"""
        data = {}
        data['players'] = {username: player.dumps() for username, player in self.players.iteritems()}
        return json.dumps(data)

    def getPlayerDict(self):
        """Returns dict of dict of online players"""
        return {username: player.__dict__ for username, player in self.players.iteritems()}

    def dictify(self):
        """Returns dict representing game data"""
        return {
            'playerdict': self.getPlayerDict()
        }
