""" application/comm.py
"""

from application import game, socketio

# @socketio.on('handshake_from_client')
# def handshake(request):
#     """Handshake pattern I've noticed is necessary in establishing connection"""
#     if request['key'] == 'initial':
#         socketio.emit('handshake_to_client', {'key': 'shake'})

# @socketio.on('player_location')
# def locationupdate(message):
#     """Docstring LOL"""
#     info = {
#         'x': message['x'],
#         'y': message['y']
#     }
#     socketio.emit('location_info', info)

@socketio.on('location update')
def location_update(message):
    game.playerlist[message['username']].x = message['x']
    game.playerlist[message['username']].y = message['y']

    game_update = {}
    for name, player in game.playerlist:
        game_update[name] = {}
        game_update[name]['x'] = player.x
        game_update[name]['y'] = player.y

    socketio.emit('game update', game_update)


@socketio.on('game close')
def game_close(message):
    if message['closed']:
        game.removeplayer(message['username'])
        game.removeclient(message['username'])
