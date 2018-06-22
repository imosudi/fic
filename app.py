#import virtualenv python library directory
import os
import sys
#sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')
sys.path.insert(0, 'venv/lib/python2.7/site-packages')


#import installed library
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_moment import Moment
from datetime import datetime
#from flask_script import Manager
from flask_wtf import FlaskForm

#Import 3rd Party
from flask_mysqldb import MySQL
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required
#from passlib.hash import sha256_crypt


#Third party imports
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

#Create application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is really hard to guess string added by Mosudi Isiaka'

# init Flask Bootstrap
bootstrap = Bootstrap(app)
moment = Moment(app)
admin = Admin(app)


#manager = Manager(app)


#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'ficplc'
app.config['MYSQL_PASSWORD'] = 'imosudi@gmail.com'
app.config['MYSQL_DB'] = 'ficplc'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MySQL
mysql = MySQL(app)


"""
python
from noteapp import db
db.create_all()
"""

from models import *


# Check user login status
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
	if 'logged_in' in session:
	    return f(*args, **kwargs)
	else:
	    flash(u'Unauthorized, Please login', 'danger')
	    return redirect(url_for('login'))
    return wrap


@app.route('/')
def home():
    page='home'
    return  render_template('index.html', page=page)

@app.route('/contact')
def contact():
	page = 'contact'
	return render_template('contact.html', page=page)


@app.route('/register')
def register():
	page= 'register'
	return render_template('register.html', page=page)

@app.route('/about')
def about():
	page= 'about'
	return render_template('about.html', page=page)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)