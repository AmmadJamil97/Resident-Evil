import os

from flask import Flask, render_template, request, session, flash, redirect
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finalproject.db")

@app.route("/")
def messages():
    usernames = db.execute("SELECT username from users;")

    MESSAGES = db.execute('SELECT * from message;')
    return render_template("chatroom.html", messages = MESSAGES, usernames=usernames)

@app.route("/message", methods =["POST", "GET"])
def message():

    if request.method == "POST":

        usernames = db.execute("SELECT username from users;")

        MESSAGES = db.execute('SELECT * from message;')
        # insert [0]["username"] at the end TRICK to remove [{'username': 'Haziq'}] and display just Haziq
        # username = db.execute("select username from users where id = ?;", session["user_id"])[0]["username"]

        db.execute = ("INSERT INTO message (message) VALUES (?)", request.form.get("message"))

        return render_template("chatroom.html", messages = MESSAGES, usernames=usernames)

    return render_template("chatroom.html", messages = MESSAGES, usernames=usernames)


@app.route("/test4")
def index():

    return render_template("test4.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods =["GET","POST"])
def login():

    # Forget any user_id either from Register or Log In earlier
    session.clear()

    if request.method == "POST":

        # go in rows for user_id from database
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # check for WRONG username exist in 2nd row (1st row is title) + OR WRONG password for that username
        if len(rows) != 1:
            return render_template("fail.html", value = "Invalid username")

        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("fail.html", value = "Invalid password")

        session["user_id"] = rows[0]["id"]

        return render_template("chatroom.html")

    # for GET
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():



    if request.method == "POST":
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("apology.html")

        # this means, else: if non of the if is true:
        # return render_template("success.html")

        # query database first into sql table
        # create a py var that execute *(all) the columns inside the username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # this means if the len of rows is 0, then new username is true, not exist yet in database(len row 1 means wherever in the db, the username occupies 1 rows in db)
        if len(rows) == 1:
            return render_template("fail.html", value = "Your username is already taken")

        # create a python variable id to combine both username and hash password and also to add session easily later on
        # this db below is to create a new row with new id and password
        id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?);",
        request.form.get("username"), generate_password_hash(request.form.get("password")))

        # to create an action cookie aka session for the current user
        session["user_id"] = id

        flash("Registered!")

        return render_template("success.html")

    # this below means, else: if request.method == "GET":
    return render_template("register.html")


@app.route("/apology")
def apology():
    return render_template("apology.html")