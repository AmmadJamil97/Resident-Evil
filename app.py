from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def route():
    name = "Ammad"
    return render_template("test3.html", name = name)
