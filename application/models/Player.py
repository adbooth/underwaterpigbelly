""" application/models/Player.py
"""


class Player(object):
    """Class for taking care of each player"""
    def __init__(self, game, username):
        game = game
        self.username = username
        self.x = 50
        self.y = 50
