from LSM303 import LSM303
import time

try:
    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"

Xmax = 0
Xmin = 0
Ymax = 0
Ymin = 0
Zmax = 0
Zmin = 0

while True:
	print "Heading :" + str(compass.getHeading())
	print ""
	time.sleep(.1)


	

