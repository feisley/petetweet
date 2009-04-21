import time
import random
from hashlib import md5

def newPassword(p):
    #Hashes the new password against a new random salt and returns salt, hpwd
    salt = newSalt()
    return salt, md5("%s_%s" % (salt , p)).hexdigest()

def hashPassword(salt, p):
    return md5("%s_%s" % (salt , p)).hexdigest()

def resetHash(username, password, logintime):
    """Generates a reset password hash based on username,
    password, and last login time. As such the hash will
    expire upon login, or change of current password"""
    
    return md5('%s_%s_%s' % (username, password, logintime)).hexdigest()

def newSalt():
    #Generates a new random salt
    return md5("%s_%s" % (random.random() , time.time())).hexdigest()