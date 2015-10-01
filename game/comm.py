""" game/comm.py
"""

from game import socketio

@socketio.on('handshake_from_client')
def handshake(request):
    """
    Handshake pattern I've noticed is necessary in establishing connection
    between client and server over socketio. This function simply receives a
    message from the client and responds.
    """
    if request['key'] == 'hand':
        socketio.emit('handshake_to_client', {'key': 'shake'})
