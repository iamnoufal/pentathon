from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlite3
from flask_session import Session


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db123.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db=SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String, unique=True)
    name = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=True)
    complaints = db.relationship("Complaint", backref="users")


class Complaint(db.Model):
    __tablename__ = "complaints"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    issue = db.Column(db.String)
    created_on = db.Column(db.String, nullable=False)
    resolved = db.Column(db.Integer)
    resolved_on = db.Column(db.String)
    # assigned_to = db.Column(db.Integer, db.ForeignKey('employees.id'))
    
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    emp_cmp_rel = db.relationship("Employee", backref="complaints")



class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employee_id = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=True)
    assigned_complain = db.Column(db.Integer, db.ForeignKey('complaints.id'))

    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host="0.0.0.0")