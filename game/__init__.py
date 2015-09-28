""" game/__init__.py
"""

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
app.debug = True

import game.views, game.comm
