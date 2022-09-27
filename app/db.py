from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

engine = None
base = declarative_base()
db = SQLAlchemy()