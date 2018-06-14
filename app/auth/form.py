from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Email


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')




class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email  =StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')