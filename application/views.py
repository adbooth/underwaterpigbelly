""" application/views.py
"""

from flask import render_template, redirect, url_for, request, session

from application import app, game
from Forms import StartForm

@app.route('/')
def index():
    """
    Root of web application
    Decides where to route user depending on cookies
    """
    # session.permanent = True
    # session.permanent_session_lifetime = True
    # if 'hascookie' in session and session['hascookie']:
    #     return redirect(url_for('play'))
    #
    # session['hascookie'] = False
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

@app.route('/play')
def play():
    """Renders game view for user"""
    return render_template('play.html')

# @app.route('/login')
# def login():
#     """Renders login view for user"""
#     return render_template('login.html')
