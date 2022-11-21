from flask import Flask, session, render_template, request, redirect


app = Flask(__name__)

@app.route("/")
@app.route("/test4.html")
def route():
    return render_template("test4.html")

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    # if method of requesting from the HTML page is POST
    if request.method == "POST":

        # Ensure all 3 field required ODNE in html from

        # Ensure password combination match
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("apology.html")

    else:
        return render_template("register.html")


@app.route("/login.html")
def blog():
    return render_template("login.html")

