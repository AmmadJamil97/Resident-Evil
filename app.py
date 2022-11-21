from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def route():
    return render_template("test4.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    # if method of requesting from the HTML page is POST
    if request.method == "POST":

        # Ensure all 3 field required ODNE in html from

        # Ensure password combination match
        if request.form.get("password") != request.form.get("confirmation")


