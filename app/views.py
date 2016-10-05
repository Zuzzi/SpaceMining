from flask import render_template, flash, redirect
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
	return render_template("login.html", form = form)
