from sid_test_mag import LSM303
import time
import random

# some type of weighing, that add up to a heading (weights add to 1)

try:
    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"


# for generating random numbers with weights
my_list = [1] * 10 + [2] * 10 + [3] * 70 + [4] * 10

# can change these, using what guide had
Xtime = 0
#Xtime = random.choice(my_list)
Ptime = 1
while True:
    Xtime = 0
    Ptime = 1
    for x in range(0, 500):
        Z = compass.getHeading()
        #Z = random.choice(my_list)
        #print "Measured:", Z
        Kupdate = Ptime / (Ptime + 0.1)  # R = 0.1, it's what guide did
        Xupdate = Xtime + Kupdate * (Z - Xtime)
        Pupdate = (1 - Kupdate) * Ptime

        Xtime = Xupdate
        Ptime = Pupdate

        #print "New estimate:", Xupdate
        #print "New error cov:", Pupdate, "\n"
        #if (x == 10 or x == 50 or x == 75):
        #    raw_input("Enter to continue...")

    print "New estimate:", Xupdate
    print "New error cov:", Pupdate, "\n"
