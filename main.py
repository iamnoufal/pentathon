from flask import Flask
import os

from app.db import db
from app.models import *

current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "db.sqlite3")

db.init_app(app)
# api = Api(app)
# app.app_context().push()

@app.route("/")
def home():
  a = User()
  a.user_id = "Noufal"
  a.name = "Noufal"
  a.pwd="password"
  print(a, "------------===============------------")
  db.session.add(a)
  db.session.commit()
  print('committed')
  return "<h4>Hello World</h4><p>How are you?</p>"

if __name__ == "__main__":
  app.run(
    host="0.0.0.0", 
    debug=True
  )
