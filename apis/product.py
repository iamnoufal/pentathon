from dataclasses import field
import marshal
from flask_restful import Resource
from flask_restful import fields, marshal_with
from flask_restful import reqparse
from app.db import db
from app.models import *
from .validations import *
from sqlalchemy import exc
from datetime import datetime

# prodIn = reqparse.RequestParser()
# prodIn.add_argument("product_id")
# prodIn.add_argument("country")

prodOut = {
  "id": fields.Integer,
  "product_id": fields.String,
  "warranty": fields.Integer,
  "warranty_end_date": fields.String,
  "product_name": fields.String
}

class ProductAPI(Resource):
  @marshal_with(prodOut)
  def get(self, product_id):
    try:
      product = Product.query.filter_by(product_id = product_id).one()
    except exc.NoResultFound:
      raise NotFoundError(code = 404, emsg = "Product Not Found")
    else:
      return product