""" application/views.py
"""

# import string, random

from flask import render_template, redirect, url_for, request, session, json

from application import app, game, socket
from Forms import StartForm

@app.route('/')
def index():
    """
    Root of web application
    Will someday decide where to route user depending on cookies
    """
    return redirect(url_for('start'))

@app.route('/start', methods=['POST', 'GET'])
def start():
    """Renders start view for user"""
    form = StartForm()
    if form.validate_on_submit():
        username = request.form['username']
        try:
            game.addplayer(username)
        except ValueError:
            form.username.errors.append('Username taken. Really, be more original')
        else:
            session['username'] = username
            return redirect(url_for('play'))

    return render_template('start.html', form=form)

@app.route('/play', methods=['POST', 'GET'])
def play():
    """Renders game view for user, as well as handles AJAX call for initial player data"""
    if request.method == 'POST':
        # Send message to all clients saying player added
        player = game.getplayer(session['username'])
        socket.emit('PLAYER_ADDED', player.__dict__)

        # Send new client initial data
        return json.dumps({
            'username': player.username,
            'player_data': player.dumps(),
            'enemy_data': game.dumps()
        })

    return render_template('play.html')
