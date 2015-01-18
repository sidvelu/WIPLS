import Adafruit_BBIO.GPIO as GPIO
import time


clk = "P8_26"
direction = "P8_13"

x = int(input("Enter Direction(1 c, 0 cc): "))

#Setting up clk and direction
GPIO.setup(clk, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)

#Setting Direction
if(x == 1):
	GPIO.output(direction, GPIO.LOW)
if(x == 0):
	GPIO.output(direction, GPIO.HIGH)

step = 0
step_limit = 1000
while(step not step_limit):
	#GPIO.output(direction, GPIO.HIGH)
	print "clk low "
	GPIO.output(clk, GPIO.LOW)
	time.sleep(.0001)
	print "clk high "
	#GPIO.output(direction, GPIO.LOW)
	GPIO.output(clk, GPIO.HIGH)
	time.sleep(.0001)
	step = step + 1
	
