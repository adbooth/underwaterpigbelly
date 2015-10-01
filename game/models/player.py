""" game/models.py
"""

from game import socketio
from game import db


class Player:
    def __init__(self, username):
        self.username = username
