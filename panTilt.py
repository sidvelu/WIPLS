# Written by Sanjeewa with love
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

upPin = "P8_27"
downPin = "P8_29"
leftPin = "P8_43"
rightPin = "P8_45"


class panTilt:

    def __init__(self):
        #Setting up GPIO pins for left,right,up,down
		
		GPIO.setup(upPin, GPIO.OUT)
		GPIO.setup(downPin, GPIO.OUT)
		GPIO.setup(leftPin, GPIO.OUT)
		GPIO.setup(rightPin, GPIO.OUT)

    #Toggling relays for pan and tilt
	def left(self)
		GIPO.output(leftPin,GPIO.HIGH)
		GIPO.output(rightPin,GPIO.LOW)
		GIPO.output(upPin,GPIO.LOW)
		GIPO.output(downPin,GPIO.LOW)
		print ("Panning Left")
		
	def right(self)
		GIPO.output(leftPin,GPIO.LOW)
		GIPO.output(rightPin,GPIO.HIGH)
		GIPO.output(upPin,GPIO.LOW)
		GIPO.output(downPin,GPIO.LOW)
		print ("Panning Right")
		
	def up(self)
		GIPO.output(leftPin,GPIO.LOW)
		GIPO.output(rightPin,GPIO.LOW)
		GIPO.output(upPin,GPIO.HIGH)
		GIPO.output(downPin,GPIO.LOW)
		print ("Tilting Up")
		
	def down(self)
		GIPO.output(leftPin,GPIO.LOW)
		GIPO.output(rightPin,GPIO.LOW)
		GIPO.output(upPin,GPIO.LOW)
		GIPO.output(downPin,GPIO.HIGH)
		print ("Tilting Down")
		
	def stop(self)
		GIPO.output(leftPin,GPIO.LOW)
		GIPO.output(rightPin,GPIO.LOW)
		GIPO.output(upPin,GPIO.LOW)
		GIPO.output(downPin,GPIO.LOW)
		print ("Motion Stop")
