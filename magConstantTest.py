from LSM303 import LSM303
import time


try:
    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"

minutes = float(raw_input("Minutes to take heading readings: "))
start_time = time.time()

counter = 0
sum = 0
while time.time() - start_time < 60 * minutes:
    #print time.time() - start_time
    sum += compass.getHeading(False)
    counter += 1

print "Average heading over", minutes , "minutes:", sum / counter