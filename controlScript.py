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

#Setting up compass, GPS, panTilt, & XBee
compass = LSM303()
GPS = GPS()
panTilt = PanTilt()
xbee = XBee()

def align(panTilt):
    panTilt.left()  # always start at left barrier
    time.sleep(52)  # time takes from one barrier to another
    panTilt.stop()

RATE = 6.8  # rate constant, in degrees per second
degrees = 180
datapoints = 10
debug = True

panTilt.stop()
#align(panTilt)
# get setup options
folderName = "run"
#direction = raw_input("Enter direction (l or r): ")
#degrees = raw_input("Enter degrees to pan: ")
#datapoints = raw_input("Enter number of datapoints: ")
os.system("rm -rf /root/Data_" + folderName)
os.system("mkdir /root/Data_" + folderName)

# get GPS coords
coords = GPS.getCoordinates()
if coords != 0:
    xbee.send("coords: " + str(coords))
else:
    xbee.send("ERROR: GPS coords not found, no fix?")

SLEEP_TIME = (degrees / datapoints) / RATE
print str(SLEEP_TIME)

if debug:
    f = open('control_debug.log', 'w')

# start loop to pan
for x in range(0,2):
    if debug:
        f.write('Starting loop ' + str(x) + '\n')
    print "starting ", x, " run"
    # get initial heading
    startHeading = compass.getAvgHeading()
    if (startHeading == 0):
        xbee.send("ERROR: startHeading is 0, heading not obtained?")
    print "Start heading: " + str(startHeading)
    if (x == 0):
        direction = "r"
    elif (x == 1):
        direction = "l"

    counter = 0
    currHeading = int(startHeading)
    while counter < datapoints:
        if (direction == "r"):
            panTilt.right()
        elif (direction == "l"):
            panTilt.left()
        
        time.sleep(SLEEP_TIME)
        panTilt.stop()
        execfile("/root/WIPLS/GNU_v3.py")
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
        os.system("mv passband_sig.bin /root/Data_" + folderName + "/passband_signal_"+ str(round(currHeading)) + ".bin")
        print("Finished one heading")

        counter += 1
        print str(counter)

    if debug:
        f.write('Finished loop processing data ' + str(x) + '\n')

    os.system("octave /root/WIPLS/processData_new.m /root/Data_" + folderName) # produces angle.txt file
    
    if debug:
        f.write('Finished processing data ' + str(x) + '\n')

    # send strongest angle via XBee to computer
    try:
        ang_file = open('/root/angle.txt', 'r')
        xbee.send("strong angle: " + str(ang_file.read()))
        f.write('angle successfully sent\n')
    except:
        xbee.send("ERROR: angle.txt file not found")
        f.write('angle.txt file not found\n')

    os.system('rm /root/Data_' + folderName + '/*')

    if debug:
        f.write('finished loop starting next ' + str(x) + '\n')

panTilt.stop()
