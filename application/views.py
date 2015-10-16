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
    Decides where to route user depending on cookies
    """
    # try:
    #     previoususer = request.cookies['previoususer']
    # except KeyError:
    #     # Make new remember cookie and store it on client
    # clientid = ''
    # while True:
    #     clientid = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in xrange(32))
    #     if not game.clientidexists(clientid):
    #         game.addclient(clientid, '')
    #         break
    #
    # response = make_response(redirect(url_for('start')))
    # response.set_cookie('clientid', clientid)
    # return response
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

    # Render start template on GET or form fail
    return render_template('start.html', form=form)

@app.route('/play', methods=['POST', 'GET'])
def play():
    """Renders game view for user, as well as handles AJAX call for initial player data"""
    if request.method == 'POST':
        socket.emit('player added', {'username': session['username'], 'x': game.getplayer(session['username']).x, 'y': game.getplayer(session['username']).y})
        return json.dumps({'username': session['username'], 'x': game.getplayer(session['username']).x, 'y': game.getplayer(session['username']).y})
    return render_template('play.html')

# @app.route('/login')
# def login():
#     """Renders login view for user"""
#     return render_template('login.html')
