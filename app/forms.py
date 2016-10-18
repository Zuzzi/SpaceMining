from flask.ext.wtf import Form
from wtforms.validators import Email, InputRequired, EqualTo
from wtforms import StringField, PasswordField, SelectField, TextAreaField, FileField
from .utility import *


class LoginForm(Form):
	username = StringField('Username', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])


class AddReportForm(Form):
	type = SelectField("Type", choices = [("harvesting","harvesting"), ("maintenance","maintenance"), ("problem","problem")])
	description = TextAreaField(validators=[InputRequired()])


class AddCurriculumForm(Form):
	name = StringField('Name', validators=[InputRequired()])
	last_name = StringField('Last Name', validators=[InputRequired()])
	email = StringField('Email', validators=[Email()])
	cv = FileField("Curriculum", validators=[InputRequired()])
	

class AddUserForm(Form):
	username = StringField('Username', validators=[InputRequired()])
	password = PasswordField('New Password', validators = [InputRequired(), EqualTo('password_confirm')])
	password_confirm  = PasswordField('Repeat Password')
	role = SelectField("Role", choices = [("miner","miner"), ("admin","admin")])
	station = SelectField("Station", choices = getStationsList())


	
