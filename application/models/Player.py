""" application/models/Player.py
"""

from application import socketio


class Player(object):
    """Player object for taking care of each player"""
    def __init__(self, username):
        self.username = username
