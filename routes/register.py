from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *


@app.route("/warranty/Replacement_register/<product_id>")
def statuscheck(product_id):
    try:
        status = Complaint.query.filter_by(product_id=product_id).one()
    except exc.NoResultFound:
        return render_template("status.html", status="")
    else:
        return render_template("status.html", status=status)


@app.route("/warranty/Replacement_register", method=["POST"])
def caller():
    caller = Caller()
    resp = request.form
    resp.headers['fill to register Product Replacement'] = '*'
    caller.Employee_name = request.form['name']
    caller.Employee_id = request.form['id']
    caller.user_id = request.form['user_id']
    caller.product_id = request.form['product_id']
    caller.reason = request.form['reason']
