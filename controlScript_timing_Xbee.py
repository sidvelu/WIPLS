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
import serial

from LSM303 import LSM303
from GPS import GPS
from PanTilt import PanTilt
from XBee import XBee

def getHeading():
    sum = 0
    for x in range(0,10):
        sum += compass.getHeading(False)
    avgHeading = sum / 10
    return avgHeading

#Setting up compass, GPS, panTilt, & XBee
compass = LSM303()
GPS = GPS()
panTilt = PanTilt()
xbee = XBee()

RATE = 6.8  # rate constant, in degrees per second

panTilt.stop()

# get setup options
folderName = raw_input("Enter Test Name: ")
#startHeading = raw_input("Enter start heading: ")
direction = raw_input("Enter direction (l or r): ")
degrees = raw_input("Enter degrees to pan: ")
datapoints = raw_input("Enter number of datapoints: ")
os.system("mkdir Data_" + folderName)

try:
    degrees = int(degrees)
except ValueError:
    print "Invalid number for degrees."
try:
    datapoints = int(datapoints)
except ValueError:
    print "Invalid number for datapoints."

# get initial heading
startHeading = getHeading()
print "Start heading: " + str(startHeading)
xbee.send("heading: " + str(startHeading))

# get GPS coords
coords = GPS.getCoordinates()
if heading != 0:
    xbee.send("coords: " + str(coords))
else:
    xbee.send("GPS coords not found.\n")

counter = 0
SLEEP_TIME = (degrees / datapoints) / RATE
print str(SLEEP_TIME)
currHeading = int(startHeading)
while counter < datapoints:
    if (direction == "r"):
        panTilt.right()
    elif (direction == "l"):
        panTilt.left()
        
    time.sleep(SLEEP_TIME)
    panTilt.stop()
    execfile("GNU_v3.py")
    if(direction == 'l'):
        currHeading -= SLEEP_TIME * RATE
    elif(direction == 'r'):
        currHeading += SLEEP_TIME * RATE

    if currHeading < 0:
        currHeading %= 360
    if currHeading > 0:
        currHeading %= 360
    print "currHeading: ", currHeading
    #rename signal files
    os.system("mv passband_sig.bin Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
    print("Finished one heading")

    counter += 1
    print str(counter)

os.system("octave processData_new.m Data_" + folderName) # produces angle.txt file

# send strongest angle via XBee to computer
ang_file = open('angle.txt', 'r')
xbee.send(ang_file.read())

panTilt.stop()
