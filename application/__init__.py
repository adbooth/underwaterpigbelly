""" application/__init__.py
"""

from os import urandom

from flask import Flask
from flask_socketio import SocketIO

from models.Game import Game

app = Flask(__name__)
app.debug = True
app.secret_key = urandom(24)
socketio = SocketIO(app)

game = Game()

import application.comm, application.views
