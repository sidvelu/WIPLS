__author__ = 'siddharth'

from MAG3110 import MAG3110
import time

try:
	mag = MAG3110()
	print "I2C Bus is accessible"
except:
	print "Error in opening up I2C Bus"



while True:
    #X = mag.magReadX()
    #jY = mag.magReadY()
    #Z = mag.magReadZ()
    heading  = mag.getHeading()


    print "Heading :" + str(heading)
    print ""
    time.sleep(.1)
