from mag_functions import MAG3110
import time

try:
	mag = MAG3110()
	print "I2C Bus is accessible"
except:
	print "Error in opening up I2C Bus"

while True:
	print "X :" + str(mag.magRead("X"))
	print "Y :" + str(mag.magRead("Y"))
	print "Z :" + str(mag.magRead("Z"))
	print ""
	time.sleep(1) 
