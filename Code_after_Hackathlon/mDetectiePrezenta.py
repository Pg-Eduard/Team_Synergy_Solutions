import RPi.GPIO as GPIO
import time
from mLumini import writeFile, updateLed, updateArray

sensor = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

def on_gpio_signal(channel):
    obj = updateArray()
    status_led_baie = obj[3]

    if obj[3] == 0:
        writeFile(2) #2 baia
        updateLed(False)
        print("data transmisa")

GPIO.add_event_detect(sensor,GPIO.FALLING,callback=on_gpio_signal,bouncetime = 1000)


def sensePresence():
    detected = GPIO.input(sensor)
    return detected