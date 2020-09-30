from flask_wtf import FlaskForm
from wtforms import FileField, validators,TextField, SubmitField, TextAreaField, SelectField, DateField, HiddenField, IntegerField, ValidationError, PasswordField
from wtforms.validators import Length, Email, InputRequired
from wtforms.fields.html5 import DateField
# from wtforms_components import PhoneNumberField

# import phonenumbers

# # Form ORM
class MainForm(FlaskForm):            
        csv = FileField('CSV File:  ')