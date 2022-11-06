from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def route():
    return render_template("test.html")