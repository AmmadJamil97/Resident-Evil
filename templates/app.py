from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)

@app.route("/test3.html")
def route():
    return render_template("test3.html")
