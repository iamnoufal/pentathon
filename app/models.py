from enum import unique
from .db import db

class Product(db.Model):
  __tablename__ = "products"
  id = db.Column(db.Integer, primary_key = True)
  product_id = db.Column(db.String, unique = True, nullable = False)
  product_name = db.Column(db.String, nullable = False)
  warranty = db.Column(db.Integer)
  warranty_end_date = db.Column(db.String)

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  user_id = db.Column(db.String, unique = True)
  name = db.Column(db.String, nullable = False)
  pwd = db.Column(db.String, nullable = True)
  complaints = db.relationship("Complaint", backref = "complaints")

class Complaint(db.Model):
  __tablename__ = "complaints"
  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  issue = db.Column(db.String)
  created_on = db.Column(db.String, nullable = False)
  resolved = db.Column(db.Integer)
  resolved_on = db.Column(db.String)
  assigned_to = db.Column(db.Integer, db.ForeignKey('employees.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Employee(db.Model):
  __tablename__ = "employees"
  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  employee_id = db.Column(db.String, unique = True)
  name = db.Column(db.String, nullable = False)
  pwd = db.Column(db.String, nullable = True)
  assigned_complain = db.Column(db.Integer, db.ForeignKey('complaints.id'))