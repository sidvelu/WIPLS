__author__ = 'siddharth'

from MAG3110 import MAG3110
import time

try:
	mag = MAG3110()
	print "I2C Bus is accessible"
except:
	print "Error in opening up I2C Bus"


prevHeading = 999
f = open('magData.txt', 'w')

for x in range(0, 20):  # 2 seconds
    heading  = mag.getHeading()
    print "Heading: " + str(heading)
	
    if (abs(heading - prevHeading) > 1):
        text = "Heading: " + str(heading) + " Time: " + time.asctime() + " \n" 
	f.write(str(heading)+"\n")	
	#print text
	prevHeading = heading

    time.sleep(.1)
f.close()


