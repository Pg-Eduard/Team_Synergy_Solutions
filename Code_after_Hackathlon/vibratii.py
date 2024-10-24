import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime as time
import re

vibratii = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibratii,GPIO.IN)

def on_gpio_signal(channel):
    scriere()

GPIO.add_event_detect(vibratii,GPIO.FALLING,callback=on_gpio_signal,bouncetime = 1000)

def citire():
        file = open("/home/eduardPi/Desktop/Programe licenta/Vibratii/detectie.txt")
        open("/home/eduardPi/Desktop/Programe licenta/Vibratii/detectie.txt").close()
        data = file.read()
        return data

def scriere():
    fisier = open("/home/eduardPi/Desktop/Programe licenta/Vibratii/detectie.txt","w")
    current_time = time.now()
    time_DHM = current_time.strftime("%D %H %M")
    fisier.write(time_DHM)