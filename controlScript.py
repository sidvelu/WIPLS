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
    #Getting Heading
    heading = getHeading()
    currHeading = getHeading()

    diff = abs(currHeading - heading)
    print "Heading: " + str(heading)
    panTilt.stop()
    raw_input("press key to continue")
    panTilt.right()
    time.sleep(13)
    '''
    while (diff <= 90):
        panTilt.stop()
        time.sleep(2)
        currHeading = getHeading()
        diff = abs(currHeading - heading)
        panTilt.right()
        time.sleep(1)
        print ","
        print diff
        print ",",
    panTilt.stop()
    print "End Heading: ", currHeading
    print "Moved 90 degrees going left"
    '''
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

align()

#Folder Setup
folderName = raw_input("Enter Test Name")
os.system("mkdir Data_" + folderName)

#Getting Heading
startHeading = getHeading()
print "Start Heading: " + str(startHeading)

while (abs(startHeading - getHeading()) <= 180):
    currHeading = getHeading()
    while (abs(getHeading() - currHeading) <= 10):
        panTilt.left()
        time.sleep(.2)
    panTilt.stop()
    execfile("GNU_v3.py")
   #rename signal files
    print "Heading Change: " + str(abs(getHeading() - currHeading))
    os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
    print("Finished one heading")
    answer = raw_input("Press Enter to Continue")
    #answer = raw_input("Press Enter to Continue, or Q to quit")
    #if answer == 'q' or answer == 'Q':
    #    break
align()

