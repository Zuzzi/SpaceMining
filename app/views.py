from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
	return render_template ("index.html")

@app.route("/hiring")
def hiring():
	#fake data
	job_positions = [{"position" : "Miner", 
	                  "description" : "Entry-level miner for SMI lunar settlement", 
				      "requirements": "None",
				      "picture" : "moon"},
				        
				      {"position" : "Medic",  
				      "description" : "Hospital staff member for asteroid-23A",
					  "requirements" : "Master Degree in Medicine",
					  "picture" : "asteroid"},
					  
					  {"position" : "Senior miner",
					  "description" : "Expert crane driver for lunar settlement",
					  "requirements" : "5 years of experience",
					  "picture" : "moon"}]
	
	return render_template("hiring.html", job_positions = job_positions)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template("login.html", form = form)
