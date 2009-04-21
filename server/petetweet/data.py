"""
Datastore Objects
"""


from google.appengine.ext import db
from google.appengine.api import users


class User(db.Model):
  username = db.StringProperty(required=True)
  password = db.StringProperty(required=True)
  firstname = db.StringProperty(required=True)
  lastname = db.StringProperty(required=True)
  email = db.EmailProperty()
  reg_date = db.DateTimeProperty(auto_now_add=True)
  last_date = db.DateTimeProperty(auto_now_add=True)

class Tweet(db.Model):
  user = db.ReferenceProperty(User)
  post_date = db.DateProperty(auto_now_add=True)
  text = db.TextProperty()