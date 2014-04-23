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

def getHeading():
    sum = 0
    for x in range(0, 10):
        sum += compass.getHeading()
    avgHeading = sum / 10

def move(direction, angle):
    time = 5
    heading = getHeading()
    while (abs(getHeading - heading) <= angle):
        prevHeading = getHeading()
        if direction == "left":
            panTilt.left()
        elif direction == "right":
            panTilt.right()
        time.sleep(time)
        panTilt.stop()
        time.sleep(.1)
        degMoved = abs(prevHeading - getHeading())
        rate = degMoved / time
        degsToGo = abs(getHeading()


 - heading)
        time = 

        rate = 

    

#Setting up compass, GPS, and panTilt
compass = LSM303()
GPS = GPS()
panTilt = PanTilt()


move("left",90)

#Folder Setup
folderName = raw_input("Enter Test Name")
os.system("mkdir Data_" + folderName)

#Getting Heading
startHeading = getHeading()
print "Start Heading: " + str(startHeading)



    

for x in range(0,50):
    currHeading = compass.getHeading()
    execfile("GNU_v3.py")
    os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
    panTilt.right()
    time.sleep(1)
    panTilt.stop()
    
