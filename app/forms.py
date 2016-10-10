from flask.ext.wtf import Form
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, SelectField, TextAreaField


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddReportForm(Form):
	type = SelectField("Type", choices = [("harvesting","harvesting"), ("maintenance","maintenance"), ("problem","problem")])
	description = TextAreaField(validators=[DataRequired()])

	
