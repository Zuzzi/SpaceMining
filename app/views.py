from flask import render_template, flash, redirect
from app import app

@app.route("/")
@app.route("/index")
def index():
	return render_template ("index.html")

@app.route("/hiring")
def hiring():
	return render_template("hiring.html")

@app.route("/login")
def login():
	return render_template("login.html")
