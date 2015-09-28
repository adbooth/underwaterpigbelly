# game/views.py

from game import app
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('game'))

@app.route('/play')
def game():
    return render_template('game.html')
