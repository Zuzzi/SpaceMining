from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm
from app import db, models

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
				else:
					print("Wrong PASSWORD!")
			else:
				print("Wrong USERNAME!")
			
			
	
	return render_template("login.html", form = form)
