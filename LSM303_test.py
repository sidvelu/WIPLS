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
	sum = 0
	for x in range(0,6):
		sum += compass.getHeading()
		time.sleep(.01)
	avg = sum / 6
	#print "Heading :" + str(compass.getHeading())
	print "Average heading:", avg
	print ""
#	time.sleep(.1)


	

