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

        # Ensure user submit a username
        if not request.form.get("username"):
            return render_ template("must provide username")


