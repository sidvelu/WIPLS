# Written by Sanjeewa with love
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

upPin = "P8_14"
downPin = "P8_18"
leftPin = "P8_12"
rightPin = "P8_16"

class PanTilt:
    def __init__(self):
        #Setting up GPIO pins for left,right,up,down	
        GPIO.setup(upPin, GPIO.OUT)
        GPIO.setup(downPin, GPIO.OUT)
        GPIO.setup(leftPin, GPIO.OUT)
        GPIO.setup(rightPin, GPIO.OUT)

    #Toggling relays for pan and tilt
    def left(self):
        GPIO.output(leftPin,GPIO.HIGH)
        GPIO.output(rightPin,GPIO.LOW)
        GPIO.output(upPin,GPIO.LOW)
        GPIO.output(downPin,GPIO.LOW)
        print ("Panning Left")
		
    def right(self):
        GPIO.output(leftPin,GPIO.LOW)
        GPIO.output(rightPin,GPIO.HIGH)
        GPIO.output(upPin,GPIO.LOW)
        GPIO.output(downPin,GPIO.LOW)
        print ("Panning Right")
		
    def up(self):
        GPIO.output(leftPin,GPIO.LOW)
        GPIO.output(rightPin,GPIO.LOW)
        GPIO.output(upPin,GPIO.HIGH)
        GPIO.output(downPin,GPIO.LOW)
        print ("Tilting Up")
		
    def down(self):
        GPIO.output(leftPin,GPIO.LOW)
        GPIO.output(rightPin,GPIO.LOW)
        GPIO.output(upPin,GPIO.LOW)
        GPIO.output(downPin,GPIO.HIGH)
        print ("Tilting Down")
		
    def stop(self):
        GPIO.output(leftPin,GPIO.LOW)
        GPIO.output(rightPin,GPIO.LOW)
        GPIO.output(upPin,GPIO.LOW)
        GPIO.output(downPin,GPIO.LOW)
        print ("Motion Stop")
