from appengine_utilities.sessions import Session
from data import *

def register(username, password, firstname, lastname, email):
    
    q = User.all()
    q.filter("username =", username)
    if q.count(1) != 0:
        raise ValueError("You cannot register an in use username")
        
    u = User(username = username,
             password = password,
             firstname = firstname,
             lastname = lastname,
             email = email)
    
    result = u.put()
       
    return "Success"

def login(username, password):
    
    q = User.all()
    q.filter("username =", username)
    user = q.get()
    
    if user and user.password == password:
        s = Session()
        s['user'] = user
        return user
    else:
        raise ValueError("Invalid username or password")
        

def status():
    s = Session()
    return s['user']
    

def post(text):
    s = Session()
    s['user']
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
