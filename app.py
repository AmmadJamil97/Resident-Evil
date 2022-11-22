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
    # validate submission
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")


    # Confirm Registration(this is else n plz care for indentation)
    return render_template("success.html")



@app.route("/login.html")
def blog():
    return render_template("login.html")
