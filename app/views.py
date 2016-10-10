from flask import render_template, flash, redirect, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from .forms import LoginForm, AddReportForm
from app import db, models, lm
from .models import User
import datetime

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
	if form.validate_on_submit() and request.method == "POST":
		request_username = request.form["username"]
		request_password = request.form["password"]
		print("Login request for username: " + request_username + " with password: " + request_password)
		user = models.User.query.filter_by(username= request_username).first()
		if user is not None:
			permitted = user.verify_password(request_password)
			if permitted:
				print("You have permission to log in")
				login_user(user)
				if user.role == "miner":
					next = "station_status"
				elif user.role == "admin":
					pass
				return redirect(url_for(next))
			else:
				print("Wrong PASSWORD!")
		else:
			print("Wrong USERNAME!")
	return render_template("login.html", form = form)
	
	
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/station_status")
@login_required
def station_status():
	print("I'm in the station status function")
	username = g.user.username
	station = models.Station.query.filter_by(name = g.user.station).first()
	return render_template("station_status.html", username = username, station = station)
	
	
@app.route("/reports_panel", methods=['GET', 'POST'])
@login_required
def reports_panel():
	form = AddReportForm()
	username = g.user.username
	reports = models.Report.query.filter_by(station = g.user.station)
	if form.validate_on_submit() and request.method == "POST":
		print("I'm in!")
		station = g.user.station
		request_type = request.form["type"]
		request_description = request.form["description"]
		timestamp = datetime.datetime.today()
		r = models.Report(type = request_type, description = request_description,
		                  miner = username, station = station, timestamp = timestamp)
		db.session.add(r)
		db.session.commit()
	return render_template("reports_panel.html", username = username, reports = reports, form = form)
	
	
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
	
	
@app.before_request
def before_request():
	g.user = current_user
