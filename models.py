#import virtualenv python library directory
import os
import sys
#sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')

sys.path.insert(0, 'venv/lib/python2.7/site-packages')


#import installed library
from flask_wtf import FlaskForm

from wtforms import Form, StringField, SubmitField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required
#from wtforms.widgets import TextArea

"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    def __init__(self, title, body):
        self.title = title
        self.body = body
"""

class registrationForm(Form):
    name = StringField('Name', [validators.Length(min=5, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    #submit = SubmitField('Complete Registeration')

    """
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')"""

class loginForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Login Password', validators=[Required()])

class createNoteForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=12)])
    body = StringField(u'Take a note', widget=TextArea())
    username = HiddenField('username')
#CREATE TABLE notes(id INT(11) AUTO_INCREMENT PRIMARY KEY, title VARCHAR(14), body VARCHAR(270), create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

class editNoteForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=12)])
    body = StringField(u'Take a note', widget=TextArea())
    author = HiddenField('author')

class deleteNoteForm(Form):
    note_id = HiddenField('note_id')

class preEditNoteForm(Form):
    note_id = HiddenField('note_id')
