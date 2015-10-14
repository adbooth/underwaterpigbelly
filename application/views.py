""" application/views.py
"""

# import string, random

from flask import render_template, redirect, url_for, request, session

from application import app, game
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

    return render_template('start.html', form=form)

@app.route('/play', methods=['POST', 'GET'])
def play():
    """Renders game view for user"""
    if request.method == 'POST':
        return session['username']
    return render_template('play.html')

# @app.route('/login')
# def login():
#     """Renders login view for user"""
#     return render_template('login.html')
