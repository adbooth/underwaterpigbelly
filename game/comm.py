# game/comm.py

from game import app, socketio

@socketio.on('fromclient')
def handshake(request):
    if request['key'] == 'hand':
        socketio.emit('toclient', {'key': 'shake'})
