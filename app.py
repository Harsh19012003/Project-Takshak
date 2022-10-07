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
# from functions import helpers


# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# APP ROUTES

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    

@app.route("/crop_recommendation", methods=["GET", "POST"])
def crop_prediction():
    # If user reached route via POST
    if request.method == "POST":
        n = request.form.get("n")
        p = request.form.get("p")
        k = request.form.get("k")
        temperature = request.form.get("temperature")
        humidity = request.form.get("humidity")
        ph = request.form.get("ph")
        rainfall = request.form.get("rainfall")

        prediction = helpers.crop_predict(n, p, k, temperature, humidity, ph, rainfall)

        return render_template("crop_result.html", prediction=prediction[0])


    # If user reached route via GET
    else:
        return render_template("crop_form.html")


@app.route("/yield_prediction", methods=["GET", "POST"])
def yieldprediction():
    # def yieldPredict(state,Crop_Year,season,crop,area,model,mydict):
    # If user reached route via POST
    if request.method == "POST":
        state = request.form.get("state")
        crop_year = request.form.get("crop_year")
        season = request.form.get("season")
        crop = request.form.get("crop")
        area = request.form.get("area")

        prediction = helpers.yield_predict(state, crop_year, season, crop, area)

        return render_template("yield_result.html", prediction = prediction)

    # If user reached route via GET
    else:
        return render_template("yield_form.html")


@app.route("/disease_detection", methods=["GET", "POST"])
def disease():
    # If user reached route via POST
    if request.method == "POST":

        #read image file string data and convert to image default
        filestr = request.files['image'].read()
        file_bytes = numpy.fromstring(filestr, numpy.uint8)
        img = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR) 
        print(type(img))

        plt.imshow(img, interpolation='nearest')
        plt.show()
        return render_template("disease_result.html")


    # If user reached route via GET
    else:
        return render_template("disease_form.html")



@app.route("/weed_detection", methods=["GET", "POST"])
def weeddetection():
    # If user reached route via POST
    if request.method == "POST":
        return render_template("weed_result.html")
    
    # If user reached route via GET
    else:
        return render_template("weed_form.html")
    


if __name__ == '__main__':
    
    app.run(debug = True)
    # webbrowser.open_new("http://127.0.0.1:5000/")