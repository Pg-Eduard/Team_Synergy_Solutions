from mLumini import updateArray
import RPi.GPIO as GPIO
from mDetectie import sendDataToExcel
import pandas as  pd
from datetime import datetime as time

def test1():
    print("hellow")

def test2():
    updateArray(1)

def test3():
    sendDataToExcel(1)

def test4():
    #fisier = open("/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx")
    #print(fisier)
    excel = pd.read_excel("/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx")
    #print(excel)

def test5():
    current_time = time.now()
    time_MY = current_time.strftime("%B %Y")
    time_DHM = current_time.strftime("%D %H %M")

    path = "/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx"
    excel = pd.read_excel(path,engine="openpyxl")
    frame = pd.DataFrame(excel)

    nr_rows = len(frame)

    my_Data = {"Date": time_MY,"Time": time_DHM,"Value": 1}
    frame.loc[nr_rows] = my_Data

    frame.to_excel("/home/eduardPi/Desktop/Programe licenta/Website/static/Data1.xlsx",index=False)

test2()
GPIO.cleanup()