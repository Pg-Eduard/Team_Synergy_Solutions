from flask import Flask, render_template, jsonify, url_for
import pandas as pd
from datetime import datetime as time
import requests
#import RPi.GPIO as GPIO
import re
from mLumini import writeFile, updateLed, updateLogo, updateArray
import json
from mDetectie import sendDataToExcel, global_getLast3Dates
from mUsi import usaGaraj, usaIntrare
from time import sleep
from vibratii import citire
from tempU import get_temp_umid
from threading import Thread

app = Flask(__name__,static_url_path="/static")

@app.route("/")
def index():
    global_start = 0
    if global_start == 0:
      updateLed(True)
      global_start = 1
    else:
       updateLed(False)
    return render_template("cod_baza.html")

@app.route("/en")
def liba_engleza():
    return render_template("Cod_baza_engleza.html")

@app.route("/sp")
def limba_spaniola():
    return render_template("Cod_baza_spaniola.html")

@app.route("/toggle_light/<int:id>")
def toggle_light(id):
  # Call writeFile function from modul_lumini
  writeFile(id)
  updateLed(False)

  # Return a success message or update data (optional)
  return "Light state updated!"

@app.route("/get_text")
def get_text():
  obj = updateArray()
  container = {}
  for i in range(len(obj)):
     if obj[i] == 0:
        container[i] = "Stins"
     else:
        container[i] = "Aprins"
  data = {
     "ledCa": container[0],
     "ledBu": container[1],
     "ledBa": container[2],
     "ledIn": container[3],
     "ledDi": container[4],
     "ledGa": container[5]
  }
  json_data = json.dumps(data)
  return jsonify(data = json_data)

@app.route("/get_detectii")
def get_detectii():
   obj = global_getLast3Dates()
   json_data = json.dumps(obj)
   return jsonify(data = json_data)

@app.route("/usa_garaj")
def usa_garaj():
   usa_garaj()
   sleep(1)
   return "Exectutat"

@app.route("/usa_intrare")
def usa_intrare():
   usaIntrare()
   sleep(1)
   return "executat"

@app.route("/vibratii")
def vibratii():
   data = citire()
   obj = {
      "activitate": data
   }
   json_data = json.dumps(obj)
   print("citit vibratii")

   return jsonify(data = json_data)

@app.route("/temp")
def temp():
   data = get_temp_umid()
   if data["valid"] == True:
      obj = {
         "temp_c": data["temp_c"],
         "umi": data["humidity"],
         "valid": "true"
      }
   else:
      obj = {
         "rezultat": "se asteapta rezultat",
         "valid": "fals"
      }
   json_data = json.dumps(obj)
   print("umitiate exectutat")
   return jsonify(data = json_data)

  
if __name__ == "__main__":
    app.run(debug = False,host = "0.0.0.0")

#GPIO.cleanup()