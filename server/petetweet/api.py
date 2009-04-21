from hashlib import md5

from appengine_utilities.sessions import Session
from data import *
import util

def register(username, password, firstname, lastname, email):
    
    q = User.all()
    q.filter("username =", username)
    if q.count(1) != 0:
        raise ValueError("You cannot register an in use username")
    
    salt, hash = util.newPassword(password)
    
    u = User(username = username,
             password = hash,
             salt = salt,
             firstname = firstname,
             lastname = lastname,
             email = email)
    
    result = u.put()
       
    return "Success"

def login(username, password):
    
    q = User.all()
    q.filter("username =", username)
    user = q.get()

    if not user:
        raise ValueError("Invalid username")

    hash = util.hashPassword(user.salt, password)
    
    if hash == user.password:
        s = Session()
        s['user'] = user
        s['status'] = True
        return user
    else:
        raise ValueError("Invalid username or password")
        

def status():
    s = Session()
    if s['status'] == True:
        return True
    else:
        return False
    

def post(text):
    s = Session()
    t = Tweet(user = s['user'],
              text = text)
    t.put()
    

def getusertweets(userid, limit = 10):

    if limit <= 0 or limit > 1000:
        raise ValueError("Limit must be from 1 - 1000")
    
    q = Tweet.all()
    q.filter("user =", userid)
    
    return q.fetch(limit)


def getalltweets(limit = 10):
    
    if limit <= 0 or limit > 1000:
        raise ValueError("Limit must be from 1 - 1000")
        
    q = Tweet.all()
    
    return q.fetch(limit)
    
def gettweets(limit = 10):
    
    if limit <= 0 or limit > 1000:
        raise ValueError("Limit must be from 1 - 1000")
    
    s = Session()
    q = Tweet.all()
    q.filter("user =", s['user'])
    
    return q.fetch(limit)
