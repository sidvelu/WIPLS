import time
import os
import sys

from XBee import XBee

#Setting up compass, GPS, panTilt, & XBee
xbee = XBee()

while True:
    print "sending"
    xbee.send("testttttt")
    time.sleep(1)

