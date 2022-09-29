from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *


@app.route("/register")
def register():
    return render_template("UserSide.html")


@app.route("/product")
def product():
    return render_template("product.html", product=None)


@app.route("/product/<product_id>")
def viewproduct(product_id):
    try:
        product = Product.query.filter_by(product_id=product_id).one()
    except exc.NoResultFound:
        return render_template("product.html", product="")
    else:
        return render_template("product.html", product=product)


@app.route("/complaint", methods=["POST"])
def postComplaint():
    complaint = Complaint()
    resp = request.form
    print(resp)
    complaint.issue = resp['desc']
    complaint.created_on = str(datetime.today())[:16]
    complaint.assigned_to = None
    complaint.product_id = resp['prodid']
    # complaint.user_id = session["user_id"]
    # complaint.user_id = 1
    try:
        db.session.add(complaint)
        db.session.commit()
    except exc.NoForeignKeysError:
        return render_template("error.html",
                               error='Session expired. Please login again to continue')
    else:
        return redirect("/")
