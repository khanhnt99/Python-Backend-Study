from wsgiref.validate import validator
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validatiors import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validator=[DataRequired()])
    password = PasswordField('Password', validator=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')