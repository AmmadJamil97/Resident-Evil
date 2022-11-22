from flask import Flask, render_template, request
from cs50 import SQL


app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finalproject.db")

@app.route("/")

@app.route("/test4")
def index():
    return render_template("test4.html")

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("apology.html")

        # this means, else: if non of the if is true:
        # return render_template("success.html")
        rows = db.execute("SELECT * FROM users WHERE username = ?", )

    # this below means, else: if request.method == "GET":
    return render_template("register.html")



@app.route("/login")
def blog():
    return render_template("login.html")


@app.route("/apology")
def apology():
    return render_template("apology.html")