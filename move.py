import Adafruit_BBIO.GPIO as GPIO
import time
import sys

clk = "P8_26"
direction = "P8_13"

#x =int( sys.argv[1] )
#step_limit = int( sys.argv[2])
#x = 1
#step_limit = 500


x = int(input("Enter Direction (1 c, 0 cc): "))
step_limit = int(input("Enter number of steps"))

print "Direction: " + str(x)
print "Step Limit: " + str(step_limit)

#Setting up clk and direction
GPIO.setup(clk, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)

#Setting Direction
if(x == 1):
	GPIO.output(direction, GPIO.LOW)
if(x == 0):
	GPIO.output(direction, GPIO.HIGH)

step = 0

while(step != step_limit):
	GPIO.output(clk, GPIO.LOW)
	time.sleep(.0001)
	GPIO.output(clk, GPIO.HIGH)
	time.sleep(.0001)
	#print "Step:"
	#print step
	step = step + 1
	
