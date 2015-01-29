from LSM303 import LSM303
import time

try:
    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"

f = open('magData.txt', 'w')

for x in range(0, 5):  # 2 seconds
    heading = compass.getHeading()
    print "Heading: " + str(heading)
    f.write(str(heading)+"\n")
    time.sleep(.1)

f.close()

