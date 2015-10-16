""" application/models/Player.py
"""

from flask import json


class Player(object):
    """Class for taking care of each player"""
    def __init__(self, game, username, x=50, y=50):
        game = game
        self.username = username
        self.x = x
        self.y = y

    @staticmethod
    def dictload(game, data):
        """Creates Player instance out of dictionary"""
        player = Player(game, data['username'])
        player.x = data['x']
        player.y = data['y']
        return player

    """
    JSON conversion stuff
    Useful because 'JSON is the language of the internet'
    """
    def dumps(self):
        """Dumps Player instance as JSON string"""
        return json.dumps(self.__dict__)

    @staticmethod
    def loads(game, string):
        """Creates Player instance out of JSON string"""
        data = json.loads(string)
        return Player.dictload(game, data)
