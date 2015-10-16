""" application/comm.py
"""

from application import game, socket

@socket.on('handshake from client')
def handshake_to_client(request):
    if request['key'] == 'hand':
        socket.emit('handshake to client', {'key': 'shake'})

# @socket.on('initial player data request')
# def initial_player_response(request):
#     initial_player_data_response = {}
#     initial_player_data_response['x'] = game.getplayer(request['username']).x
#     initial_player_data_response['y'] = game.getplayer(request['username']).y
#     socket.emit('initial player data response', initial_player_data_response)

@socket.on('location update')
def location_update(update):
    """Gets location data from a client, responds with most recent game data"""
    # Store new location data
    game.playerlist[update['username']].x = update['x']
    game.playerlist[update['username']].y = update['y']

    # Prepare game data object for response
    game_update = {}
    for name, player in game.playerlist.iteritems():
        game_update[name] = {}
        game_update[name]['x'] = player.x
        game_update[name]['y'] = player.y

    # Respond with game update
    socket.emit('game update', game_update)

# @socket.on('game close')
# def game_close(message):
#     """Removes player from player data structures on game close"""
#     if message['closed']:
#         game.removeplayer(message['username'])
#         # game.removeclient(message['username'])
