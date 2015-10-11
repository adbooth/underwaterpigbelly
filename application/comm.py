""" application/comm.py
"""

from application import socketio

@socketio.on('handshake_from_client')
def handshake(request):
    """Handshake pattern I've noticed is necessary in establishing connection"""
    if request['key'] == 'hand':
        socketio.emit('handshake_to_client', {'key': 'shake'})

@socketio.on('player_location')
def locationupdate(location):
    """Docstring LOL"""
    info = {
        'x': location['x'],
        'y': location['y']
    }
    socketio.emit('location_info', info)
