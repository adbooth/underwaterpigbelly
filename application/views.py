""" game/views.py
"""

from application import app
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    """
    Redirects user to 'play' URL
    Will probably use this later on to check the user's cookies and redirect to
    a login or setup page.
    """
    return redirect(url_for('game'))

@app.route('/play')
def game():
    """Renders game view for user"""
    return render_template('game.html')

@app.route('/login')
def login():
    """Renders login view for user"""
    return render_template('login.html')

@app.route('/start')
def start():
    """Renders start view for user"""
    return render_template('start.html')
