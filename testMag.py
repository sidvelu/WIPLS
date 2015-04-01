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
    for x in range(0,100):
        sum += compass.getHeading(False)
        time.sleep(.01)
    avg = sum / 100
    #print "Heading :" + str(compass.getHeading())
    print "Average heading:", avg
    #print "Average offset heading:", avgOffset

    sum = 0
    for x in range(0, 100):
        sum += compass.getPitch()
        time.sleep(.01)
    avg = sum / 100
    print "Pitch is: ", avg
    #print "Accl X: " , compass.readAcclX()
    #print "Accl Y: " , compass.readAcclY()
    #print "Accl Z: " , compass.readAcclZ()
    print ""
    time.sleep(1)

    '''
    print "Heading :" + str(compass.getHeading(False))
    print "Heading offset :" + str(compass.getHeading(True))
    print ""
    time.sleep(.5)
    '''


	

