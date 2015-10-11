""" application/views.py
"""

from application import app, game
from flask import render_template, redirect, url_for, request, session

@app.route('/')
def index():
    """
    Redirects user to 'play' URL
    Will probably use this later on to check the user's cookies and redirect to
    a login or setup page.
    """
    return redirect(url_for('start'))

@app.route('/play')
def play():
    """Renders game view for user"""
    username = session['username']
    return render_template('play.html', username=username)

@app.route('/login')
def login():
    """Renders login view for user"""
    return render_template('login.html')

@app.route('/start', methods=['POST', 'GET'])
def start():
    """Renders start view for user"""
    error = ''
    if request.method == 'POST':
        # It's a form submission
        form = request.form
        if not game.addplayer(form['username']):
            error = 'Username ' + form['username'] + ' already exists'

        if not error:
            session['username'] = form['username']
            return redirect(url_for('play'))

    return render_template('start.html', error=error)
