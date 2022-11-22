from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("test4.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/register.html", methods=["post"])
def register():
    # validate submission
    if not request.form.get("username"):
        return render_template("apology.html")


    # Confirm Registration(this is else n plz care for indentation)
    return render_template("test4.html")



@app.route("/login.html")
def blog():
    return render_template("login.html")
