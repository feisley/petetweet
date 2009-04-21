"""
Datastore Objects
"""


from google.appengine.ext import db
from google.appengine.api import users


class User(db.Model):
  username = db.StringProperty(required=True)
  password = db.StringProperty(required=True)
  salt = db.StringProperty(required=True)
  firstname = db.StringProperty(required=True)
  lastname = db.StringProperty(required=True)
  email = db.EmailProperty()
  reg_date = db.DateTimeProperty(auto_now_add=True)
  last_date = db.DateTimeProperty(auto_now_add=True)

class Tweet(db.Model):
  user = db.ReferenceProperty(User, collection_name='tweets')
  post_date = db.DateTimeProperty(auto_now_add=True)
  text = db.TextProperty()
  
class Message(db.Model):
  sender = db.ReferenceProperty(User, collection_name='sent_messages')
  recipient = db.ReferenceProperty(User, collection_name='received_messages')
  send_date = db.DateTimeProperty(auto_now_add=True)
  text = db.TextProperty()