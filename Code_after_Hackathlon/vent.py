import RPi.GPIO as GPIO
import time
import pandas as pd

sensor = 26
stare = 0
countdown = 2000

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.OUT)

def selectState():
    try:
        check = pd.read_excel("static/vent.xlsx")
        if check.empty:
            obj = {"State" : [0]}
            check = pd.DataFrame(obj)
        else:
            check = pd.read_excel("static/vent.xlsx")
    except:
        obj = {"State" : [0]}
        check = pd.DataFrame(obj)

    temp = check["State"][0]
    if temp == 0:
        temp = 1
        GPIO.output(sensor,GPIO.HIGH)
    else:
        temp = 0
        GPIO.output(sensor,GPIO.LOW)

    temp_obj = {"State" : [temp]}


    check = pd.DataFrame(temp_obj)
    check.to_excel("static/vent.xlsx",index=False)

    return check["State"][0]
