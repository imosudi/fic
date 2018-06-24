#import installed library
from flask_wtf import FlaskForm

from wtforms import Form, StringField, SelectMultipleField, SubmitField, RadioField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required
from wtforms.widgets import TextArea

#from flask_sqlalchemy import SQLAlchemy

from app import db

"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    def __init__(self, title, body):
        self.title = title
        self.body = body
"""

class personalForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    def __init__(self, title, body):
        self.title = title
        self.body = body


class personalForm(Form):
    first_name = StringField('First name', [validators.Length(min=5, max=50), validators.DataRequired()])
    last_name = StringField('Last name', [validators.Length(min=5, max=50), validators.DataRequired()])
    middle_name = StringField('Middle name', [validators.Length(min=5, max=50)])
    email = StringField('Email Address', [validators.Length(min=6, max=50), validators.email(), validators.DataRequired()])
    phone_number1 = StringField('Phone number', [validators.Length(min=5, max=50), validators.DataRequired()])
    phone_number2 = StringField('Alternative Phone number', [validators.Length(min=5, max=50)])
    address_line1 = StringField('Address line 1', [validators.Length(min=5, max=50), validators.DataRequired()])
    address_line2 = StringField('Address line 2', [validators.Length(min=5, max=50)])
    city = StringField('City', [validators.Length(min=5, max=50)])
    state = StringField('State', [validators.Length(min=5, max=50), validators.DataRequired()])
    lga = StringField('LGA', [validators.Length(min=5, max=50), validators.DataRequired()])

    #username = StringField('Username', [validators.Length(min=4, max=25)])
    """password = PasswordField('New Password', [
                    validators.DataRequired(),
                    validators.EqualTo('confirm', message='Passwords must match')
                ])
                confirm = PasswordField('Repeat Password')"""
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Next stage')



class businessForm(Form):
    business_name = StringField('Business name', [validators.Length(min=5, max=50), validators.DataRequired()])
    business_rc = StringField('Business Registeration Number(RC Number)', [validators.Length(min=5, max=50), validators.DataRequired()])
    business_description = StringField('Business decription ', [validators.Length(min=5, max=50)])
    website = StringField('Website http://... ', [validators.Length(min=6, max=50), validators.email(), validators.DataRequired()])
    business_email = StringField('Business Email Address', [validators.Length(min=6, max=50), validators.email(), validators.DataRequired()])
    business_phone = StringField('Business Phone number', [validators.Length(min=5, max=50), validators.DataRequired()])
    mailbox = StringField('P.O Box ', [validators.Length(min=5, max=50)])
    bus_address_line1 = StringField('Business Address line 1', [validators.Length(min=5, max=50), validators.DataRequired()])
    bus_address_line2 = StringField('Address line 2', [validators.Length(min=5, max=50)])
    bus_city = StringField('City', [validators.Length(min=5, max=50)])
    bus_state = StringField('State', [validators.Length(min=5, max=50), validators.DataRequired()])
    bus_lga = StringField('LGA', [validators.Length(min=5, max=50), validators.DataRequired()])
    bank_name = StringField('Bank name', [validators.Length(min=5, max=50), validators.DataRequired()])
    account_name = StringField('Account name', [validators.Length(min=5, max=50), validators.DataRequired()])
    account_number = StringField('NUBAN  10-digit number', [validators.Length(min=5, max=50), validators.DataRequired()])
    account_type = RadioField('Label', choices=[('Savings Account','Savings Account'), 
                                                ('Current Account','Current Account')], 
                                                validators=[Required()])
    submit = SubmitField('Next Stage')

class locationForm(Form):
    longitude1 = StringField('Longitude', [validators.Length(min=5, max=50), validators.DataRequired()])
    latitude1 = StringField('Latitude', [validators.Length(min=5, max=50), validators.DataRequired()])
    business_history= RadioField('Business History', choices=[('Existing Business&nbsp;&nbsp;' ,'Existing Business ',),
                                                     ('New Business','New Business')], 
                                                     validators=[Required()])
    business_accesibility = SelectMultipleField('Business Accesibility', 
                                            choices=[('On a Major Road','On a Major Road',),
                                                     ('Market or Shopping Mall Entrance','Market or Shopping Mall Entrance',),
                                                        ('High Traffic Business Premises','High Traffic Business Premises',),
                                                         ('Close to a Bus Stop', 'Close to a Bus Stop')],
                                                         validators=[Required()])
    accept_tos = BooleanField('[ I AGREE ] By submitting this application for our organisation to be approved as a location for the provision of Financial and Citizen services using the One Network Online Agent Management andTransaction Platform, we hereby certify that all documentation provided are correct and authorize staff or agents of One Network to conduct a verification excise based on the infomation provided.',
                            [validators.DataRequired()])
    submit = SubmitField('Submit Application')



    """
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')"""

"""class loginForm(Form):
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
"""