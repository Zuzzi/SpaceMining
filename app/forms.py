from flask.ext.wtf import Form
from wtforms.validators import DataRequired, Email
from wtforms import StringField, PasswordField, SelectField, TextAreaField, FileField


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddReportForm(Form):
	type = SelectField("Type", choices = [("harvesting","harvesting"), ("maintenance","maintenance"), ("problem","problem")])
	description = TextAreaField(validators=[DataRequired()])


class AddCurriculumForm(Form):
	name = StringField('Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	email = StringField('Email', validators=[Email()])
	cv = FileField("Curriculum", validators=[DataRequired()])
	
