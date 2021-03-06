import time
import os
import sys

# load all GNUradio modules here, so we load only once
print "Loading GNUradio modules once..."
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import baz

from LSM303 import LSM303
from GPS import GPS
from PanTilt import PanTilt

def align():
    panTilt.stop()
    raw_input("Press enter to align")
    panTilt.right()
    time.sleep(90 / RATE)
    panTilt.stop()

def getHeading():
    sum = 0
    for x in range(0,10):
        sum += compass.getHeading(False)
    avgHeading = sum / 10
    return avgHeading

#Setting up compass, GPS, and panTilt
compass = LSM303()
GPS = GPS()
panTilt = PanTilt()

# CONSTANTS TO BE SETUP
#RATE = 6.9231 # degrees per second
RATE = 6.8
DATAPOINTS = 50.0
DEGREES = 180.0

#align()
panTilt.stop()

# get setup options
print "magHeading : ", getHeading()
folderName = raw_input("Enter Test Name: ")
#startHeading = raw_input("Enter start heading: ")
direction = raw_input("Enter direction (l or r): ")
startDir = raw_input("Enter N,W,E,S: ")

if (startDir == "N"): 
    startHeading = 0
elif (startDir == "E"):
    startHeading = 90
elif (startDir == "S"):
    startHeading = 180
elif (startDir == "W"):
    startHeading = 270
else:
    sys.exit(0)

os.system("mkdir Data_" + folderName)

#print "Start Heading: " + str(startHeading)

counter = 0
SLEEP_TIME = (DEGREES / DATAPOINTS) / RATE
print str(SLEEP_TIME)
currHeading = int(startHeading)
while counter < DATAPOINTS:
    if (direction == "r"):
        panTilt.right()
    elif (direction == "l"):
        panTilt.left()
        
    time.sleep(SLEEP_TIME)
    panTilt.stop()
    execfile("GNU_v3.py")
    currHeading -= SLEEP_TIME * RATE
    if currHeading < 0:
        currHeading %= 360
    print "currHeading: ", currHeading
    print "magHeading : ", getHeading()
   #rename signal files
    os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
    print("Finished one heading")
    #answer = raw_input("Press Enter to Continue")
    #answer = raw_input("Press Enter to Continue, or Q to quit")
    #if answer == 'q' or answer == 'Q':
    #    break
    counter += 1
    print str(counter)

align()
