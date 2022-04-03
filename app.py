from flask_app import app
from flask import render_template, request, session, redirect
from userdb import creating_account
import userdb

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/newaccount", methods=["POST","GET"])
def account_creation():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        role = creating_account(username, password, role)
        session["username"] = username
        session["role"] = role
        #TODO sisäänkirjautumisen virheentarkistukset
        return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    userdb.login(username, password)
    return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")






if __name__ == '__main__':
    app.run(debug=True)
