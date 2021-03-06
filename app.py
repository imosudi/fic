from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is really hard to guess string by Mosudi Isiaka imosudi@gmail.com'

Bootstrap(app)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://imosudific:imosudificpassword@35.184.110.46/imosudific'
#sql2.freemysqlhosting.net	sql2244352	sql2244352
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


#This is actually needed by the form classes to load db.Models, so I will create
#another py file forms.py

from models import *




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



@app.route('/registration')
def registration():
	page = 'registration'
	formP = personalForm(request.form)
	formB = businessForm(request.form)
	formL = locationForm(request.form)
	return render_template('registration.html', page=page, formP=formP, formB=formB, formL=formL)


@app.route('/reg')
def reg():
	page = 'reg'
	formP = personalForm(request.form)
	formB = businessForm(request.form)
	formL = locationForm(request.form)
	if request.method == 'POST' and  formP.validate():
		name = formP.name.data
		username = formP.username.data
		email = formP.email.data
		#password = sha256_crypt.encrypt(str(form.password.data))
	return render_template('reg.html', page=page, formP=formP, formB=formB, formL=formL)





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