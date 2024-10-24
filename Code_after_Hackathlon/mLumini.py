import RPi.GPIO as GPIO
import re

dataPin = 24
clockPin = 18
latchPin = 23

input1 = 25
input2 = 8
input3 = 7
input4 = 12
input5 = 16
input6 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup((dataPin,clockPin,latchPin),GPIO.OUT)
GPIO.setup((input1,input2,input3,input4,input5,input6),GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def shift(input,data,clock,latch):
        GPIO.output(clock,0)
        GPIO.output(latch,0)
        GPIO.output(clock,1)

        GPIO.output(data,input)

        GPIO.output(clock,0)
        GPIO.output(latch,1)
        GPIO.output(clock,1)

def readFile():
        file = open("/home/eduardPi/Desktop/Programe licenta/Lumini/ddl.txt")
        open("/home/eduardPi/Desktop/Programe licenta/Lumini/ddl.txt").close()
        raw_array = file.read()
        refined_array = re.sub("\s", "",raw_array)
        functional_array = []
        for i in range(len(refined_array)):
            functional_array += refined_array[i]
        for i in range(len(functional_array)):
            functional_array[i] = int(functional_array[i])
        return functional_array
    
def writeFile(pos):
    array = readFile()
    val = array[pos]
    if val == 1:
        array[pos] = 0
    else:
        array[pos] = 1
    file = open("/home/eduardPi/Desktop/Programe licenta/Lumini/ddl.txt","w")
    for i in range(len(array)):
        file.write(str(array[i]) + " ")
    return array

def updateLed(test):
    if test == False:
            array=readFile()
    else:
            array=[1,1,1,1,1,1,1,1]
    for i in range(0,8,1):
            shift(array[i],dataPin,clockPin,latchPin)

def updateLogo():
     array = readFile()
     led = [array[1],array[2],array[3],array[4],array[5],array[6]]
     return led

def updateArray():
     array = readFile()
     arrayFizic = [GPIO.input(input1),GPIO.input(input2),GPIO.input(input3),GPIO.input(input4),GPIO.input(input5),GPIO.input(input6)]
     print("array analog: ", arrayFizic)
     return arrayFizic