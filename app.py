from ast import Import
from flask_ngrok import run_with_ngrok
import webbrowser
from importlib.metadata import requires
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import flask_session
import cv2
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import numpy
from matplotlib import pyplot as plt
import joblib

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/crop_recommendation", methods=["GET", "POST"])
def crop_prediction():
    if request.method == "POST":
        return render_template("#")
    else:
        return render_template("#")

@app.route("/yield_prediction", methods=["GET", "POST"])
def yieldprediction():
    if request.method == "POST":
        return render_template("#")
    else:
        return render_template("#")

@app.route("/disease_detection", methods=["GET", "POST"])
def disease():
    if request.method == "POST":
        return render_template("#")
    else:
        return render_template("#")

@app.route("/weed_detection", methods=["GET", "POST"])
def weeddetection():
    if request.method == "POST":
        return render_template("#")
    else:
        return render_template("#")

if __name__ == '__main__':
    
    app.run(debug = True)


        
