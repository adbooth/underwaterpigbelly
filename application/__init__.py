""" application/__init__.py
"""

from flask import Flask
from flask_socketio import SocketIO
from os import urandom

app = Flask(__name__)
app.debug = True
app.secret_key = urandom(24)
socketio = SocketIO(app)

from models.Game import Game
game = Game()

import application.comm, application.views
