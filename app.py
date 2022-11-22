from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")

@app.route("/test4")
def index():
    return render_template("test4.html")

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/register", methods=["post"])
def register():

    if request.method.get("username") != request.method.get("confirmation"):
        return render_template("apology.html")

    return render_template("register.html")



@app.route("/login")
def blog():
    return render_template("login.html")
