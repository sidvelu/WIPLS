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


def align():
    #Getting Heading
    heading = compass.getHeading()
    print "Heading: " + str(heading)
    while (abs(heading - compass.getHeading()) <= 90:
        panTilt.left()
    panTilt.stop()
    print "Moved 90 degrees going left"

#Setting up compass, GPS, and panTilt
compass = LSM303()
GPS = GPS()
panTilt = panTilt()

align()

#Folder Setup
folderName = raw_input("Enter Test Name")
os.system("mkdir Data_" + folderName)

#Getting Heading
startHeading = compass.getHeading()
print "Start Heading: " + str(startHeading)

while (abs(startHeading - compass.getHeading()) <= 180):
    currHeading = compass.getHeading()
    while (abs(compass.getHeading() - currHeading) <= 10):
        panTilt.right()
    panTilt.stop()
    execfile("GNU_v2.py")
    #rename signal files
    print "Heading Change: " + str(abs(compass.getHeading() - currHeading))
    os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(heading)) + ".bin")
    print("Finished one heading")
    answer = raw_input("Press Enter to Continue")
    #answer = raw_input("Press Enter to Continue, or Q to quit")
    #if answer == 'q' or answer == 'Q':
    #    break
align()

