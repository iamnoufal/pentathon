from flask import Flask
import os
from flask_restful import Api

from app.db import db
from app.models import *

current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "db.sqlite3")

db.init_app(app)
api = Api(app)
app.app_context().push()

app.secret_key = "secretkeyforapp"
app.app_context().push()

from routes.home import *
from routes.complaint import *
from routes.service import *
from routes.serviceAssign import *

from apis.product import *

api.add_resource(ProductAPI, "/api/product/<product_id>")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )
