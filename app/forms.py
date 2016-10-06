from flask.ext.wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
