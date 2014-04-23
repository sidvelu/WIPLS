import time
import os
import sys

# load all GNUradio modules here, so we load only once
# to reduce time to take samples
print "Loading GNUradio modules once..."
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
from LSM303 import LSM303
import baz
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
RATE = 6.9231 # degrees per second
#RATE = 7.1
DATAPOINTS = 15.0

#align()
panTilt.stop()
#Folder Setup
#folderName = raw_input("Enter Test Name: ")
startHeading = raw_input("Enter start heading: ")
#os.system("mkdir Data_" + folderName)

#Getting Heading
#startHeading = getHeading()
#print "Start Heading: " + str(startHeading)

counter = 0
SLEEP_TIME = 180.0 / DATAPOINTS / RATE
print str(SLEEP_TIME)
currHeading = int(startHeading)
while counter < DATAPOINTS:
    panTilt.left()
    time.sleep(SLEEP_TIME)
    panTilt.stop()
    time.sleep(.5)
    #execfile("GNU_v3.py")
    currHeading -= SLEEP_TIME * RATE
    if currHeading < 0:
        currHeading %= 360
    print "currHeading: ", currHeading
   #rename signal files
    #os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
    print("Finished one heading")
    #answer = raw_input("Press Enter to Continue")
    #answer = raw_input("Press Enter to Continue, or Q to quit")
    #if answer == 'q' or answer == 'Q':
    #    break
    counter += 1
    print str(counter)

align()