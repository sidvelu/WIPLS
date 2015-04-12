from LSM303 import LSM303
from PanTilt import PanTilt
from XBee import XBee
import time

#Setting up compass, GPS, panTilt, & XBee
compass = LSM303()
panTilt = PanTilt()
xbee = XBee()

#Getting XBEE Number
ID_file = open('/root/WIPLS/XBEE_ID', 'r')
XBeeNum = str(ID_file.read()).strip()

while(True):
    heading = compass.getAvgHeading()
    message = XBeeNum + " " + str(heading)
    xbee.send(message)
    time.sleep(5)
    

