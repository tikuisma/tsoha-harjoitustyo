from userdb import db
from flask import *

def login(name, password):
    if db.user_doesnt_exists(name, password):
        return False
    return True

def new_user(name, password, role):
    if db.user_doesnt_exists(name, password):
        
