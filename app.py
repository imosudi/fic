from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return  render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/register')
def register():
	return render_template('register.html')


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