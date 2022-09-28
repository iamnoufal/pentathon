from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc

@app.route("/")
def home():
  return render_template("home.html")
