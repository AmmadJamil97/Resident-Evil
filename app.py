from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/test4.html")
def index():
    return render_template("test4.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/register.html")
def register():
    # Confirm Registration(this is else n plz care for indentation)
    return render_template("register.html")



@app.route("/login.html")
def blog():
    return render_template("login.html")
