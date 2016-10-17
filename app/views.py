from flask import render_template, flash, redirect, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from .forms import LoginForm, AddReportForm, AddCurriculumForm
from app import db, models, lm
from .models import User
import datetime
from config import *
from sqlalchemy import desc
from werkzeug.utils import secure_filename

@app.route("/")
@app.route("/index")
def index():
	return render_template ("index.html")


@app.route("/hiring")
def hiring():		  
	job_positions = models.JobPosition.query.all()
	return render_template("hiring.html", job_positions = job_positions)
	
	
@app.route("/apply/<int:job_id>", methods=['GET', 'POST'])
def apply(job_id = -1):
	form = AddCurriculumForm()
	job = models.JobPosition.query.filter_by(id = job_id).first()
	if form.validate_on_submit() and request.method == "POST":
		filename = secure_filename(form.cv.data.filename)
		form.cv.data.save(UPLOAD_FOLDER + "/" + filename)
		job_app = models.JobApplication(name = request.form["name"], last_name = request.form["last_name"],
										email = request.form["email"], cv_path = UPLOAD_FOLDER + "/" + filename,
										job_id = job_id )
		db.session.add(job_app)
		db.session.commit()
		print("file saved!")
		return render_template("success.html")
	return render_template("apply.html", form = form, job = job)
	

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
					next = "log_file"
				f = models.LogFile(user = user.username, role = user.role, action = "Logged IN",
				                   timestamp = datetime.datetime.today())
				db.session.add(f)
				db.session.commit()
				return redirect(url_for(next))
			else:
				print("Wrong PASSWORD!")
		else:
			print("Wrong USERNAME!")
	return render_template("login.html", form = form)
	
	
@app.route('/logout')
def logout():
	f = models.LogFile(user = g.user.username, role = g.user.role, action = "Logged OUT",
	                   timestamp = datetime.datetime.today())
	db.session.add(f)
	db.session.commit()
	logout_user()
	return redirect(url_for('index'))


@app.route("/station_status", methods=['GET', 'POST'])
@app.route("/station_status/<int:page>", methods=['GET', 'POST'])
@login_required
def station_status(page = 1):
	username = g.user.username
	u_station = models.Station.query.filter_by(name = g.user.station).first()
	all_messages = models.Message.query.filter_by(station = u_station.name)
	messages = all_messages.paginate(page, MESSAGES_PER_PAGE, False)
	return render_template("station_status.html", username = username, station = u_station, messages = messages)
	
	
@app.route("/reports_panel", methods=['GET', 'POST'])
@login_required
def reports_panel():
	form = AddReportForm()
	username = g.user.username
	reports = models.Report.query.filter_by(station = g.user.station)
	ordered_reports = reports.order_by(desc(models.Report.timestamp))
	if form.validate_on_submit() and request.method == "POST":
		station = g.user.station
		request_type = request.form["type"]
		request_description = request.form["description"]
		timestamp = datetime.datetime.today()
		r = models.Report(type = request_type, description = request_description,
						  miner = username, station = station, timestamp = timestamp)
		db.session.add(r)
		r_id = models.Report.query.filter_by(timestamp = timestamp).first().id
		f = models.LogFile(user = g.user.username, role = g.user.role,
		                   action = "Added report " + str(r_id), timestamp = datetime.datetime.today())
		db.session.add(f)
		db.session.commit()
	return render_template("reports_panel.html", username = username, reports = ordered_reports, form = form)
	

@app.route("/log_file")
@login_required
def log_file():
	username = g.user.username
	files = models.LogFile.query.all()
	ordered_files = sorted(files, key=lambda x: x.timestamp, reverse=True)
	return render_template("log_file.html", username = username, files = ordered_files)
	

@app.route("/clear_logfile", methods=['GET', 'POST'])
@login_required
def clear_logfile():
	files = models.LogFile.query.all()
	for file in files:
		db.session.delete(file)
	db.session.commit()
	return redirect(url_for("log_file"))
	
	
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
	
	
@app.before_request
def before_request():
	g.user = current_user
