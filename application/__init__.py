""" application/__init__.py
"""

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

import application.comm, application.views
