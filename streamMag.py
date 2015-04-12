from LSM303 import LSM303
from PanTilt import PanTilt
from XBee import XBee
import time

#Setting up compass, GPS, panTilt, & XBee
compass = LSM303()
panTilt = PanTilt()
xbee = XBee()


while(True):
    heading = compass.getAvgHeading()
    message = "mag: " + str(heading)
    print message
    xbee.send(message)
    time.sleep(5)
    

