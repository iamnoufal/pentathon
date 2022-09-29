from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *


@app.route("/warranty/stat")
def status():
    return render_template("Warranty_Stat.html", status=None)


@app.route("/warranty/stat/<product_id>")
def statuscheck(product_id):
    try:
        stat = Complaint.query.filter_by(product_id=product_id).one()
    except exc.NoResultFound:
        return render_template("Warranty_Stat.html", stat="")
    else:
        return render_template("Warranty_Stat.html", status=stat)
