from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import abort, request, session
import os

def login(username, password):
    sql = "SELECT password, id, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    role = user[2]
    return username

def creating_account(username, password, role):
    hash_password = generate_password_hash(password)
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        try:
            sql = """INSERT INTO users (username, password, role)
                    VALUES (:username, :password, :role)"""
            db.session.execute(sql, {"username":username, "password":hash_password, "role":role})
            db.session.commit()
        except:
            return False
    return True