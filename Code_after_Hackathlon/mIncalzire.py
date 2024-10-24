import RPi.GPIO as GPIO
import time
import pandas as pd

sensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.OUT)

def stareIncazlire():
    try:
        check = pd.read_excel("static/incalzire.xlsx")
        if check.empty:
            obj = {"Status": [0]}
            check = pd.DataFrame(obj)
        else:
            check = pd.read_excel("static/incalzire.xlsx")
    except:
        obj = {"Status": [0]}
        check = pd.DataFrame(obj)

    if check["Status"][0] == 0:
        obj = {"Status": [1]}
        new_state = pd.DataFrame(obj)
        new_state.to_excel("static/incalzire.xlsx",index = False)
        GPIO.output(sensor,GPIO.HIGH)

    if check["Status"][0] == 1:
        obj = {"Status": [0]}
        new_state = pd.DataFrame(obj)
        new_state.to_excel("static/incalzire.xlsx",index = False)
        GPIO.output(sensor,GPIO.LOW)

