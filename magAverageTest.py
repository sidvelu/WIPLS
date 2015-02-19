#from LSM303 import LSM303
import time
import random


try:
#    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"


headings = list()

#closest = compass.getHeading(False)
closest = random.randint(0, 360)

while True:
    for x in range(0, 10):
        #headings.append(compass.getHeading(False))
        headings.append(random.randint(0, 360))
    avg = sum(headings) / len(headings)
    print "Average heading:", avg

    headings.append(closest) # add the start/closest heading to be evaluted too
    closest = min(headings, key=lambda x:abs(x-avg))
    print "Closest heading, using in next evaluation:", closest
    print sorted(headings), "\n"
    headings[:] = []  # clear the list for next iteration
    time.sleep(3)