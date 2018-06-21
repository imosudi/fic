import os
import sys
#sys.path.insert(0, '/var/www/clients/client6/web28/cgi-bin/venv/lib/python2.7/site-packages')

sys.path.insert(0, 'venv/lib/python2.7/site-packages')

from flask import render_template, request
from app import app

@app.route('/registeration', methods=['GET', 'POST'])
def registeration():
	page='registeration'
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data, form.email.data,
                    form.password.data)
		db_session.add(user)
		flash('Thanks for registering')
		return redirect(url_for('login'))

	return render_template('registeration.html', form=form, page=page)