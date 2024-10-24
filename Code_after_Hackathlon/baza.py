from flask import Flask, render_template, jsonify, url_for, request
from flask_apscheduler import APScheduler
import pandas as pd
from datetime import datetime as time
import requests
import RPi.GPIO as GPIO
import re
from mLumini import writeFile, updateLed, updateLogo, updateArray
import json
from mDetectie import sendDataToExcel, global_getLast3Dates
from mUsi import usaGaraj, usaIntrare
from time import sleep
from vibratii import citire
from tempU import get_temp_umid
from threading import Thread
from ventilator import selectState
from vreme import get_vreme
import scheduler_vreme as sv
from mDetPrezenta import sensePresence

scheduler = APScheduler()
app = Flask(__name__,static_url_path="/static")

@app.route("/api_vreme")
def api_vreme():
    date_vreme = get_vreme()
    json_data = json.dumps(date_vreme)
    return jsonify(data = json_data) #nou

@scheduler.task("interval",id="check_presence", seconds=10)
def check_presence():
    detection = sensePresence()
    obj = updateArray()
    if obj[3] == 1:
        if detection == 0:
            writeFile(2)
            updateLed(False)

@scheduler.task('interval', id='check_weather', seconds=60) #nou
def check_weather():
    sv.day_time()
    sv.vreme()
    print("executat task")

@app.route("/")
def index():
    return render_template("pagina_logare.html")

@app.route("/", methods=['GET',"POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("pass")

    if username == username and password == password:
        print(f"Username: {username}, Password: {password}")
        return render_template("pagina_logare.html")
    else:
        return "Username si parola sunt necesare", 400  #login
    
@app.route('/logare', methods=['POST'])
def logare():
    # Preluam datele trimise de formular sub forma de JSON
    user_existent = False
    user_index = 0
    counter = 0
    counter_pass = 0
    data = request.get_json()
    username_web = data.get('username')
    password_web = data.get('password')
    print(username_web,password_web)

    try:
        test = pd.read_excel("static/user_database.xlsx")
        if test.empty:
            database = pd.DataFrame()
        else:
            database = pd.read_excel("static/user_database.xlsx")
    except:
        database = pd.DataFrame()

    database_users = database["user"].tolist()
    database_pass = database["pass"].tolist()

    for users in database_users:
        counter += 1
        print(counter)
        if users == username_web:
            print("user exists")
            user_index = database_users.index(users)
            break
        elif counter >= len(database_users):
            return jsonify(success=False, message="Username-ul este gre?it", field="username")
    print(database_pass[user_index])
    
    if password_web != str(database_pass[user_index]):
        print(type(password_web),type(database_pass[user_index]))
        return jsonify(success=False,message="Parola este gresita", field = "pass")

    return jsonify(success=True)  #login

@app.route("/save_users",methods=["POST"])
def createExcel():
    try:
        test_date = pd.read_excel("static/user_database.xlsx")
        if test_date.empty:
            print("Fisierul este gol, se creeaza un dataframe gol")
            login_info = pd.DataFrame()
        else:
            print("Date detectate in fisier, se incarca datele")
            login_info = pd.read_excel("static/user_database.xlsx")
    except:
        print("eroare in accesarea datelor, se creaza un dataframe gol")
        login_info = pd.DataFrame()

    try:
        data = request.get_json()
        username = data.get('username_sign')
        password = data.get("password_sign")

        db_users = login_info['user'].tolist()
        for users in db_users:
            if username == users:
                print("user existent detectat")
                return jsonify(success=False, message="Utilizatorul exista deja",field = "username_sign")

        date_de_adaugat = {
            "user": [username],
            "pass": [password]
        }
        date_noi = pd.DataFrame(date_de_adaugat)

        date_combinate = pd.concat([login_info,date_noi],ignore_index=True)

        date_combinate.to_excel("static/user_database.xlsx",index=False)

        return jsonify(success=True)
    
    except:
        data = request.get_json()
        username = data.get("username_sign")
        password = data.get("password_sign")
        date_de_adaugat = {
            "user": [username],
            "pass": [password]
        }
        date_noi = pd.DataFrame(date_de_adaugat)
        date_noi.to_excel("static/user_database.xlsx",index=False)
        return jsonify(success=True)  #login
    
@app.route("/check_avalability")
def check_avalability():
    max_users = 4
    try:
        check = pd.read_excel("static/user_database.xlsx")
        if check.empty:
            check = pd.DataFrame()
        else:
            print("date detectate")
            check = pd.read_excel("static/user_database.xlsx")
    except:
        print("eroare in accesarea datelor")
        check = pd.DataFrame()

    try:
        no_users = len(check["user"].tolist())

        if no_users >= max_users:
            return jsonify(over_limit=True)
        else:
            return jsonify(over_limit=False)
    except:
        return jsonify(over_limit=False) #login

@app.route("/ro")
def limba_romana():
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
  writeFile(id)
  updateLed(False)
  print(updateArray())

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
     "ledCa": container[4],
     "ledBu": container[5],
     "ledBa": container[3],
     "ledIn": container[2],
     "ledDi": container[1],
     "ledGa": container[0]
  }
  print(container[0],container[1],container[2],container[3],container[4],container[5])
  json_data = json.dumps(data)
  return jsonify(data = json_data)

@app.route("/get_detectii")
def get_detectii():
   obj = global_getLast3Dates()
   json_data = json.dumps(obj)
   return jsonify(data = json_data)

@app.route("/usa_garaj")
def usa_garaj():
   usaGaraj()
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

@app.route("/vent")
def vent():
   selectState()
   return("executat")

@app.route("/temp")
def temp():
   try:
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
   except:
      obj = {
            "rezultat": "se asteapta rezultat",
            "valid": "fals"
         }
      json_data = json.dumps(obj)
      print("umitiate exectutat")
      return jsonify(data= json_data)

  
if __name__ == "__main__":
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug = False,host = "0.0.0.0")

GPIO.cleanup()