import time
import os
import sys
import serial

from LSM303 import LSM303
from GPS import GPS
from PanTilt import PanTilt

if len(sys.argv) != 3:
    print "Error invalid paramaters"
    print "Enter as: testMove (l,r) (degrees)"
    sys.exit()

print "argv: ", str(sys.argv)
print "direction: ", str(sys.argv[1])
print "degrees: ", str(sys.argv[2])


# get setup options
direction = str(sys.argv[1])
degrees = int(sys.argv[2])

def getHeading():
    sum = 0
    for x in range(0,10):
        sum += compass.getHeading(False)
    avgHeading = sum / 10
    return avgHeading

#Setting up compass, GPS, and panTilt
#compass = LSM303()
#GPS = GPS()
panTilt = PanTilt()

# CONSTANTS TO BE SETUP
#RATE = 6.9231 # degrees per second 
RATE = 6.8 
#DATAPOINTS = 10.0
#DEGREES = 180.0

#align()
panTilt.stop()


SLEEP_TIME = (degrees) / RATE
print "Time to sleep" , SLEEP_TIME

if (direction == "r"):
    panTilt.right()
elif (direction == "l"):
    panTilt.left()
        
time.sleep(SLEEP_TIME)
panTilt.stop()

