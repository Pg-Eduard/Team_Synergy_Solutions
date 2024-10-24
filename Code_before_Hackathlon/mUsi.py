import RPi.GPIO as GPIO
from time import sleep
import re

GPIO.setmode(GPIO.BCM)
GPIO.setup((16,12,4), GPIO.OUT)


# Set up the PWM on pin #16 at 50Hz
pwm = GPIO.PWM(16, 50)
pwm1 = GPIO.PWM(12,50)

def unghi_procent (unghi) :
    if unghi > 180 or unghi < 0 :
        return False

    start = 4
    end = 12.5
    ratie = (end - start)/180

    unghi_ca_procent = unghi * ratie

    return start + unghi_ca_procent

def usaGaraj():
    semnal = open("/home/eduardPi/Desktop/Programe licenta/Usi/garaj.txt").read()
    refined_array = re.sub("\s", "",semnal)
    array = [int(refined_array[0])]
    
    if array[0] == 0:
        pwm.start(unghi_procent(90))
        sleep(1)
        pwm.ChangeDutyCycle(unghi_procent(180))
        sleep(1)
        pwm.stop()
        with open("/home/eduardPi/Desktop/Programe licenta/Usi/garaj.txt", "w") as fisier:
            fisier.write(str(1))
            fisier.close()
    elif array[0] == 1:
        pwm.start(unghi_procent(180))
        sleep(1)
        pwm.ChangeDutyCycle(unghi_procent(90))
        sleep(1)
        pwm.stop()
        with open("/home/eduardPi/Desktop/Programe licenta/Usi/garaj.txt", "w") as fisier:
            fisier.write(str(0))
            fisier.close()


def usaIntrare():
    semnal = open("/home/eduardPi/Desktop/Programe licenta/Usi/intrare.txt").read()
    refined_array = re.sub("\s", "",semnal)
    array = [int(refined_array[0])]
    
    if array[0] == 0:
        pwm1.start(unghi_procent(90))
        sleep(1)
        pwm1.ChangeDutyCycle(unghi_procent(180))
        sleep(1)
        pwm1.stop()
        with open("/home/eduardPi/Desktop/Programe licenta/Usi/intrare.txt", "w") as fisier:
            fisier.write(str(1))
            fisier.close()
    elif array[0] == 1:
        pwm1.start(unghi_procent(180))
        sleep(1)
        pwm1.ChangeDutyCycle(unghi_procent(90))
        sleep(1)
        pwm1.stop()
        with open("/home/eduardPi/Desktop/Programe licenta/Usi/intrare.txt", "w") as fisier:
            fisier.write(str(0))
            fisier.close()