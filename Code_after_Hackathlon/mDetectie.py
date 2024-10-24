from flask import Flask, render_template, jsonify, url_for
import pandas as pd
from datetime import datetime as time
import requests
import RPi.GPIO as GPIO

graph_url = "https://thingspeak.com/channels/2396349/charts/1?bgcolor=%23ffffff&color=%23d62020&results=60&title=Detectie"
global_ulr_request = "https://api.thingspeak.com/update?api_key=FTVTR3J07CX6SK0T&field1=1"

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)

def on_gpio_signal(channel):
    requests.get(global_ulr_request)
    sendDataToExcel(1)
    print("data transmisa")

GPIO.add_event_detect(27,GPIO.FALLING,callback=on_gpio_signal,bouncetime = 1000)

def global_getLast3Dates():
    return_obj = {
        "data1": "",
        "data2": "",
        "data3": ""
    }

    path = "/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx"
    excel = pd.read_excel(path)
    frame = pd.DataFrame(excel)

    rl = len(frame)

    return_obj["data1"] = "Date: " + str(frame.at[frame.index[rl-1],"Date"]) + " " + str(frame.at[frame.index[rl-1],"Time"]) + " " + str(frame.at[frame.index[rl-1],"Value"])
    return_obj["data2"] = "Date: " + str(frame.at[frame.index[rl-2],"Date"]) + " " + str(frame.at[frame.index[rl-2],"Time"]) + " " + str(frame.at[frame.index[rl-2],"Value"])
    return_obj["data3"] = "Date: " + str(frame.at[frame.index[rl-3],"Date"]) + " " + str(frame.at[frame.index[rl-3],"Time"]) + " " + str(frame.at[frame.index[rl-3],"Value"])
    return return_obj

def sendDataToExcel(value):
    current_time = time.now()
    time_MY = current_time.strftime("%B %Y")
    time_DHM = current_time.strftime("%D %H %M")

    try:
        check = pd.read_excel("static/Data1.xlsx")
        if check.empty:
            obj = {"Date": time_MY,"Time": time_DHM,"Value":value}
            check = pd.DataFrame(obj)
        else:
            print("date detectate")
            check = pd.read_excel("static/Data1.xlsx")
            obj = {"Date": time_MY,"Time": time_DHM,"Value":value}
    except:
        print("eroare in accesarea datelor")
        obj = {"Date": [time_MY],"Time": [time_DHM],"Value":[value]}
        check = pd.DataFrame(obj)
    
    frame = pd.DataFrame(check)

    nr_rows = len(frame)

    my_Data = {"Date": time_MY,"Time": time_DHM,"Value": value}
    frame.loc[nr_rows] = my_Data

    frame.to_excel("/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx",index=False)