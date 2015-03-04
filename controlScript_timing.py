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

def align():
    panTilt.stop()
    raw_input("Press enter to align")
    panTilt.right()
    time.sleep(degrees / RATE)
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
#DATAPOINTS = 10.0
#DEGREES = 180.0

#align()
panTilt.stop()

# get setup options
folderName = raw_input("Enter Test Name: ")
startHeading = raw_input("Enter start heading: ")
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

#Getting Heading
#startHeading = getHeading()
#print "Start Heading: " + str(startHeading)

o_heading = open("info.txt", "w")
heading  = GPS.getCoordinates()
if heading != 0:
    o_heading.write("Tracker GPS Coordinates:\n")
    o_heading.write('\t\t"lat:" ')
    o_heading.write("-" if heading[1] == 'S' else "")
    o_heading.write(str(heading[0]) + "\n")
    o_heading.write('\t\t"long:" ')
    o_heading.write("-" if heading[3] == 'W' else "")
    o_heading.write(str(heading[2]) + "\n")
    o_heading.close()
else:
    o_heading.write("GPS heading not found.\n")
os.system("mv info.txt Data_" + folderName + "/info.txt")


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
    #answer = raw_input("Press Enter to Continue")
    #answer = raw_input("Press Enter to Continue, or Q to quit")
    #if answer == 'q' or answer == 'Q':
    #    break
    counter += 1
    print str(counter)

os.system("octave processData_new.m Data_" + folderName) # produces angle.txt file
# insert XBee send to computer

#align()
panTilt.stop()
