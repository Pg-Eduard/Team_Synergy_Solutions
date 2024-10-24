import RPi.GPIO as GPIO
import time
import pandas as pd

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.OUT)
# low = on, high = off, status = 1 -> off, status = 0 -> on

def stareLumini_ext():
    try:
        check = pd.read_excel("static/ext.xlsx")
        if check.empty:
            obj = {"Status": [0]}
            check = pd.DataFrame(obj)
        else:
            check = pd.read_excel("static/ext.xlsx")
    except:
        obj = {"Status": [0]}
        check = pd.DataFrame(obj)

    if check["Status"][0] == 0:
        obj = {"Status": [1]}
        new_state = pd.DataFrame(obj)
        new_state.to_excel("static/ext.xlsx",index = False)
        GPIO.output(sensor,GPIO.HIGH)

    if check["Status"][0] == 1:
        obj = {"Status": [0]}
        new_state = pd.DataFrame(obj)
        new_state.to_excel("static/ext.xlsx",index = False)
        GPIO.output(sensor,GPIO.LOW)