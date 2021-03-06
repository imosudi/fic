#import installed library
from flask_wtf import FlaskForm

from wtforms import Form, StringField, SelectMultipleField, SubmitField, RadioField, IntegerField, HiddenField, validators, BooleanField, PasswordField
from wtforms.validators import Required
from wtforms.widgets import TextArea

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

class PersonalForm(db.Model):
    __tablename__ = 'PersonalForm'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    middle_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    phone_number1 = db.Column(db.String(60), index=True, unique=True)
    phone_number2 = db.Column(db.String(60), index=True)
    address_line1 = db.Column(db.String(160), index=True)
    address_line2 = db.Column(db.String(160), index=True)
    city = db.Column(db.String(60), index=True)
    state = db.Column(db.String(60), index=True)
    lga = db.Column(db.String(60), index=True)
    
    def __init__(self, first_name, last_name, middle_name, email, phone_number1,
                phone_number2, address_line1, address_line2, city, state, lga):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.email = email
        self.phone_number1 = phone_number1
        self.phone_number2 = phone_number2
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.lga = lga

class BusinessForm(db.Model):
    __tablename__ = 'BusinessForm'
    id = db.Column(db.Integer, primary_key=True)
    business_name = db.Column(db.String(60), index=True)
    business_rc = db.Column(db.String(60), index=True)
    business_description = db.Column(db.String(60), index=True)
    website = db.Column(db.String(60), index=True)
    business_email = db.Column(db.String(60), index=True)
    business_phone =  db.Column(db.String(60), index=True)
    mailbox = db.Column(db.String(60), index=True)
    bus_address_line1 = db.Column(db.String(60), index=True)
    bus_address_line2 = db.Column(db.String(60), index=True)
    bus_city = db.Column(db.String(60), index=True)
    bus_state = db.Column(db.String(60), index=True)
    bus_lga = db.Column(db.String(60), index=True)
    bank_name = db.Column(db.String(60), index=True)
    account_name =  db.Column(db.String(60), index=True)
    account_number = db.Column(db.String(60), index=True)
    account_type = db.Column(db.String(60), index=True)

    
    def __init__(self, business_name, business_rc, business_description, website,
                business_email, business_phone, mailbox, bus_address_line1, bus_address_line2,
                bus_city, bus_state, bus_lga, bank_name, account_name, account_number, account_type):
        self.business_name = business_name
        self.business_rc = business_rc
        self.business_description = business_description
        self.website = website
        self.business_email = business_email
        self.business_phone = business_phone
        self.mailbox = mailbox
        self.bus_address_line1 = bus_address_line1
        self.bus_address_line2 = bus_address_line2
        self.bus_city = bus_city
        self.bus_state = bus_state
        self.bus_lga = bus_lga
        self.bank_name = bank_name
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type

class LocationForm(db.Model):
    __tablename__ = 'LocationForm'
    id = db.Column(db.Integer, primary_key=True)
    longitude1 = db.Column(db.String(60), index=True)
    latitude1 = db.Column(db.String(60), index=True)
    business_history = db.Column(db.String(60), index=True)
    business_accesibility = db.Column(db.String(60), index=True)
    accept_tos = db.Column(db.String(60), index=True)

    def __init__(self, longitude1, latitude1, business_history, business_accesibility, accept_tos):
        self.longitude1 = longitude1
        self.latitude1 = latitude1
        self.business_history = business_history
        self.business_accesibility = business_accesibility
        self.accept_tos = accept_tos
    

        
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
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Next stage')

    def validate_email(self, field):
        if PersonalForm.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    

    #username = StringField('Username', [validators.Length(min=4, max=25)])
    """password = PasswordField('New Password', [
                    validators.DataRequired(),
                    validators.EqualTo('confirm', message='Passwords must match')
                ])
                confirm = PasswordField('Repeat Password')"""



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
    business_history = RadioField('Business History', choices=[('Existing Business&nbsp;&nbsp;' ,'Existing Business ',),
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