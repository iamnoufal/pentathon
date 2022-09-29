from flask import current_app as app
from flask import request, redirect, render_template, session
from datetime import date, datetime
from sqlalchemy import exc
from app.models import *


@app.route("/service")
def Assignservice():
    return render_template("Service.html")


@app.route("/Assignservice", meathods=["POST"])
def assignservice(service_description):
    service = Service()
    resp = request.form
    resp.headers['fill out this service data'] = '*'
    service.warranty_id = resp["desc"]
    service.user_id = session["user_id"]
    service.product_getdate = str(datetime.date())
    service.product_Returndate = str(datetime.date())
    description = service.service_description.data
    service.service_description = request.get(description)
    try:
        db.session.add(service)
        db.session.commit()
    except:
        if (service.product_getdate < datetime.date.today()) or (
                service.product_Returndate < datetime.date.today()):
            raise ValueError("Data Cannot be in the Past!!!")
        elif exc.NoForeignKeysError:
            return render_template("error.html",
                                   error='Session expired. Please login again to continue')
    finally:
        return redirect("/Assignservice")
