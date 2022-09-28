from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *

@app.route("/register")
def register():
  return render_template("UserSide.html")

@app.route("/complaint", methods=["POST"])
def postComplaint():
  complaint = Complaint()
  resp = request.form
  complaint.issue = resp['desc']
  complaint.created_on = str(datetime.today())[:16]
  complaint.assigned_to = None
  complaint.user_id = session["user_id"]
  try:
    db.session.add(complaint)
    db.session.commit()
  except exc.NoForeignKeysError:
    return render_template("error.html", error = 'Session expired. Please login again to continue')
  finally:
    return redirect("/complaint")