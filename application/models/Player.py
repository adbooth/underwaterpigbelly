""" application/models/Player.py
"""


class Player(object):
    """Player object for taking care of each player"""
    def __init__(self, game, username):
        game = game
        self.username = username
