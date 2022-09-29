from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *


@app.route("/warranty/Complain_register/<product_id>")
def statuscheck(product_id):
    try:
        status = Complaint.query.filter_by(product_id=product_id).one()
    except exc.NoResultFound:
        return render_template("status.html", status="")
    else:
        return render_template("status.html", status=status)


@app.route("/warranty/Complain_register", method=["POST"])
def caller():
    caller = Caller()
    resp = request.form
    resp.headers['fill to register Complain'] = '*'
    caller.name = request.form['name']
    caller.user_phone = request.form['phone']
    caller.user_pincode = request.form['location']
    caller.product_id = request.form['product_id']
    caller.reason = request.form['reason']
