from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class JobPosition(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	job = db.Column(db.String(120))
	description = db.Column(db.String(120))
	requirements = db.Column(db.String(120))
	picture = db.Column(db.String(60))

	def __repr__(self):
		return '<Job %r>' % (self.job)
		

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), index = True, unique = True)
	password = db.Column(db.String(60))
	password_hash = db.Column(db.String(128))
	role = db.Column(db.String(60))
	station = db.Column(db.String(120))
	
	@property
	def password(self):
		raise AttributeError("password is not a readable attribute!")
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def __repr__(self):
		return "<User %r>" % (self.username)
		
	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3
		

class Station(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), index = True, unique = True)
	location = db.Column(db.String(120))
	oxygen =  db.Column(db.Integer)
	food = db.Column(db.Integer)
	crew = db.Column(db.Integer)
	alarm = db.Column(db.Boolean)
	
	def __reprs__(self):
		return '<Station %r>' % (self.name)
		

class Report(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	station = db.Column(db.String(120))
	miner = db.Column(db.String(60))
	type = db.Column(db.String(60))
	description = db.Column(db.Text)
	
	def __reprs__(self):
		return '<Report %r>' % (self.description)

