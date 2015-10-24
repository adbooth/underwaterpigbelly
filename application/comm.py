""" application/comm.py
"""

from application import game, socket

@socket.on('HANDSHAKE_FROM_CLIENT')
def handshake_to_client(request):
    """Handshake pattern I've noticed is necessary to open connection"""
    if request['payload'] == 'hand':
        socket.emit('SERVER_MESSAGE', {
            'command': 'HANDSHAKE_TO_CLIENT',
            'username': request['username'],
            'payload': 'shake'
        })

@socket.on('LOCATION_UPDATE')
def game_udpate(update):
    """Gets location data from a client, responds with most recent game data"""
    # Store new location data
    game.updatePlayer(update['username'], update['x'], update['y'])
    # Respond with game update
    socket.emit('SERVER_MESSAGE', {
        'command': 'GAME_UPDATE',
        'username': update['username'],
        'payload': game.dictify()
    })

@socket.on('GAME_CLOSE')
def game_close(message):
    """Removes player from playerlist on game close"""
    socket.emit('SERVER_MESSAGE', {
        'command': 'PLAYER_REMOVED',
        'payload': message.username
    })
    game.removePlayer(message['username'])
