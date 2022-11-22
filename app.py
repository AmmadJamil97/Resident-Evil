from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test4.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/lalaport", methods=["get", "post"])
def register():



@app.route("/login.html")
def blog():
    return render_template("login.html")
