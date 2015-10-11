""" application/models/Game.py
"""

from application import app


class Game(object):
    """Game object for taking care of global game data"""
    def __init__(self):
        self.playerlist = []
