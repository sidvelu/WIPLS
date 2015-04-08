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


panTilt = PanTilt()

RATE = 6.8 

panTilt.stop()

SLEEP_TIME = (degrees) / RATE
print "Time to sleep" , SLEEP_TIME

if (direction == "r"):
    panTilt.right()
elif (direction == "l"):
    panTilt.left()
        
time.sleep(SLEEP_TIME)
panTilt.stop()

