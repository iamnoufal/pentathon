from enum import unique
from .db import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String, unique=True, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    warranty = db.Column(db.Integer)
    warranty_end_date = db.Column(db.String)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String, unique=True)
    name = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=True)
    complaints = db.relationship("Complaint", backref="complaints")


class Complaint(db.Model):
    __tablename__ = "complaints"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    issue = db.Column(db.String)
    created_on = db.Column(db.String, nullable=False)
    resolved = db.Column(db.Integer)
    resolved_on = db.Column(db.String)
    assigned_to = db.Column(db.Integer, db.ForeignKey('employees.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employee_id = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=True)
    assigned_complain = db.Column(db.Integer, db.ForeignKey('complaints.id'))


class Service(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    service_id = db.Column(db.String, unique=True)
    warranty_id = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_getdate = db.Column(db.String, nullable=False)
    product_Returndate = db.Column(db.String, nullable=False)
    service_description = db.Column(db.String, nullable=False)


class Caller(db.Model):
    __tabelname__ = "Service"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, unique=True)
    user_phone = db.Column(db.Integer)
    user_pincode = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.String, unique=True)
    reason = db.Column(db.String(300), nullable=False)
    Warranty_num = db.Column(db.String, autoincrement=True, unique=True)
