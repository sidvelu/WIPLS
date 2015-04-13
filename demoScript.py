import time
import os
import sys
import serial

from LSM303 import LSM303
from GPS import GPS
from PanTilt import PanTilt

if len(sys.argv) != 3:
    print "Error invalid paramaters"
    print "Enter as: testMove (l,r,u,d) (degrees)"
    sys.exit()

print "argv: ", str(sys.argv)
print "direction: ", str(sys.argv[1])
print "degrees: ", str(sys.argv[2])


# get setup options
direction = 0
degrees = 180


panTilt = PanTilt()

RATE = 6.8 

panTilt.stop()

SLEEP_TIME = (degrees) / RATE
print "Time to sleep" , SLEEP_TIME

while(True):
    if (direction == 0):
        panTilt.right()
    elif (direction == 1):
        panTilt.left()
        
    time.sleep(SLEEP_TIME)
    panTilt.stop()
    direction += 1
    direction %= 2

