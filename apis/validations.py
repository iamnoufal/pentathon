from werkzeug.exceptions import HTTPException
from flask import make_response
import json

class NotFoundError(HTTPException):
  def __init__(self, code, emsg):
    self.response = make_response(emsg, code)

class ValidationError(HTTPException):
  def __init__(self, code, ecode, emsg):
    data = {
      "error_code": ecode,
      "error_message": emsg
    }
    self.response = make_response(json.dumps(data), code)

class DuplicateError(HTTPException):
  def __init__(self, code, emsg):
    self.response = make_response(emsg, code)