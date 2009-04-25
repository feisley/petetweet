from hashlib import md5

from appengine_utilities.sessions import Session
from data import *
import util

import logging


def NotLoggedInError(Exception):
    pass
    

def loginRequired():
    if status == False:
        raise NotLoggedInError("You must be authenticated to use this API call")
    

def register(username, password, firstname, lastname, email):
    
    if (len(password) < 6 ):
        raise ValueError("Your password needs to be at least 6 characters long")
    
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
        raise ValueError("Invalid username or password")

    hash = util.hashPassword(user.salt, password)
    
    if hash == user.password:
        s = Session()
        s['user'] = user
        s['status'] = True
        return user
    else:
        raise ValueError("Invalid username or password")
        

def logout():
    s = Session()
    s.delete();

def status():
    s = Session()
    try:
        if s['status'] == True:
            return True
        else: raise KeyError
    except KeyError:
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
    q.filter("user =", db.Key(userid))
    q.order("-post_date")
    
    return q.fetch(limit)


def getalltweets(limit = 10):
    
    if limit <= 0 or limit > 1000:
        raise ValueError("Limit must be from 1 - 1000")
        
    q = Tweet.all()
    q.order("-post_date")
    
    return q.fetch(limit)
    
def gettweets(limit = 10):
    
    if limit <= 0 or limit > 1000:
        raise ValueError("Limit must be from 1 - 1000")
    
    s = Session()
    q = Tweet.all()
    q.filter("user =", s['user'])
    q.order("-post_date")
    
    return q.fetch(limit)

def search(str):
    
    # Check usernames
    q = User.all();
    q.filter("username =", str)
    r1 = q.fetch(10)
    
    # Check firstname
    q = User.all();
    q.filter("firstname =", str)
    r2 = q.fetch(10)
    
    # Check lastname
    q = User.all();
    q.filter("lastname =", str)
    r3 = q.fetch(10)
    
    # Check email
    q = User.all();
    q.filter("email =", str) 
    r4 = q.fetch(10)
    
    rx = r1 + r2 + r3 + r4
    
    logging.info(r1)
    logging.info(r2)
    logging.info(r3)
    logging.info(r4)
    
    def f(x):
        return x.key() in rx
    
    # Build Result set
    f = filter(f, rx)
    logging.info(f)
    
    return r1;

def getMyProfile():
    if status:
        s = Session();
        q = User.all()
        q.filter("__key__ =", s["user"])
        
        return q.get()

def updateMyProfile(userid, firstname, lastname, email, password):

    q = User.all()
    q.filter("__key__ =", db.Key(userid))
    user = q.get()
    
    user.firstname = firstname
    user.lastname = lastname
    user.email = email
    
    if (password != None):
        user.password = util.hashPassword(user.salt, password)
    
    #Commit changes to store
    user.save()

def getProfile(userid):
    
    q = User.all()
    q.filter("__key__ =", db.Key(userid))
    
    return q.get()
    
    
def follow(userid):
    
    s = Session()
    me = s['user']
    them = db.Key(userid)
    
    f = Follow(follower = me, followee = them)
    

def unfollow(userid):
    
    s = Session()
    me = s['user']
    them = db.Key(userid)
    
    q = Follow.all()
    q.filter("follower =", me)
    q.filter("followee =", them)
    q.get();
    
    f = Follow(follower = me, followee = them)

def checkFollower(userid):
    
    s = Session()
    me = s['user']
    them = db.Key(userid)
    
    q = Follow.all()
    q.filter("follower =", them)
    q.filter("followee =", me)
    c = q.count();
    
    if c > 0:
        return True
    else:
        return False

def checkFollowing(userid):

    s = Session()
    me = s['user']
    them = db.Key(userid)
    
    q = Follow.all()
    q.filter("follower =", me)
    q.filter("followee =", them)
    c = q.count();
    
    if c > 0:
        return True
    else:
        return False

def follerwers():
    
    s = Session()
    me = s['user']
    them = db.Key(userid)
    
def following():

    s = Session()
    me = s['user']
    them = db.Key(userid)
    
    