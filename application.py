from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main/emptyclasses")
def show():
    # ABDULLAH BU KISIM SENDE
    return "here are the empty classes"

@app.route("/main/people")
def see():
    return render_template("people.html")



