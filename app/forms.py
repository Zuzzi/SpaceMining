from flask.ext.wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
