""" application/Forms.py
"""

from flask_wtf import Form
from wtforms import StringField, validators

# from models.Game import game

class StartForm(Form):
    """Start form"""
    username = StringField('Choose a username:', validators=[validators.DataRequired(), validators.Length(min=5, max=20)])

    # def validate_unique_name(form, field):
    #     if game.
