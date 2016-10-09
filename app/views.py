from flask import render_template, flash, redirect, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from .forms import LoginForm
from app import db, models, lm
from .models import User

@app.route("/")
@app.route("/index")
def index():
	return render_template ("index.html")


@app.route("/hiring")
def hiring():			  
	job_positions = models.JobPosition.query.all()
	return render_template("hiring.html", job_positions = job_positions)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if request.method == "POST":
			request_username = request.form["username"]
			request_password = request.form["password"]
			print("Login request for username: " + request_username + " with password: " + request_password)
			u = models.User.query.filter_by(username= request_username).first()
			if u is not None:
				permitted = u.verify_password(request_password)
				if permitted:
					print("You have permission to log in")
					login_user(u)
					return redirect(url_for("%s_home" % (u.role)))
				else:
					print("Wrong PASSWORD!")
			else:
				print("Wrong USERNAME!")
	return render_template("login.html", form = form)
	
	
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/miner_home")
@login_required
def miner_home():
	print("I'm in")
	username = g.user.username
	return render_template("miner_home.html", username = username)
	
	
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
	
	
@app.before_request
def before_request():
	g.user = current_user
