import RPi.GPIO as GPIO
from time import sleep
from pigpio_dht import DHT11


GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.IN)
gpio = 11 # BCM Numbering

sensor = DHT11(gpio)

def get_temp_umid():
    result = sensor.read()
    if result["valid"] == "False":
        result = sensor.read()
    return result

print(get_temp_umid())