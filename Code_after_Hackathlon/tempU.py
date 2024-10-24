import RPi.GPIO as GPIO
from time import sleep
from pigpio_dht import DHT11

sensor = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

sensor = DHT11(sensor)

def get_temp_umid():
    try:
        result = sensor.read()
        if result["valid"] == "False":
            result = sensor.read()
        return result
    except:
        return "success"

print(get_temp_umid())