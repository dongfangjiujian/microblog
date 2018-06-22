from flask_wtf import FlaskForm
from wtforms.validators import Email,EqualTo,DataRequired
from wtforms import SubmitField,StringField,PasswordField,BooleanField
from app.models import User
from app.auth.form import RegisterForm

class UserModifyForm(FlaskForm):

    username = StringField('Username',validators=[DataRequired()])

    email=StringField('Email',validators=[Email(),DataRequired()])
    admin = BooleanField('Administrator')
    submit = SubmitField('Modify')

