import time
import math
import os
from Adafruit_I2C import Adafruit_I2C


# I2C address constants
os.system('i2cdetect -y -r 1')
ACCL = Adafruit_I2C(0x32 >> 1) # 1B
MAG = Adafruit_I2C(0x3C >> 1, debug=True, busnum=1)  # 1E

# MAG register constants
LSM303_REGISTER_MAG_CRA_REG_M = 0x00
LSM303_REGISTER_MAG_CRB_REG_M = 0x01
LSM303_REGISTER_MAG_MR_REG_M = 0x02

print str(hex(MAG.address))
#ACCL.write8(0x20, 0x57)
os.system('i2cdetect -y -r 1')
time.sleep(.00001)
while True:
	try:
		r1 = MAG.write8(LSM303_REGISTER_MAG_MR_REG_M, 0x01)
		time.sleep(.001)
		r2 = MAG.write8(LSM303_REGISTER_MAG_CRB_REG_M, 0x60)  # +- 2.5 Gauss
		if (r1 == -1 or r2 == -1):
			raise Exception("")
		os.system('i2cdetect -y -r 1')
		break
	except:
		print ""



#print "0x01 Register " + str( MAG.readS8(0x01))

time.sleep(1)
# LSM303DLHC has no WHOAMI register so read CRA_REG_M to check
# the default value (0b00010000/0x10)

while True:
	try:
		r1 = MAG.readS8(LSM303_REGISTER_MAG_CRA_REG_M)
		time.sleep(.001)
		if (r1 == -1):
			raise Exception("")
		break
	except:
		print ""

print "READ COMPLETE"

time.sleep(1)

def readAccl( register):
	lo = ACCL.readU8(register)
	time.sleep(.0001)
	hi = ACCL.readS8(register + 1)
	return  (hi << 8) + lo


def readMag( register):
	hi = MAG.readU8(register)
	time.sleep(.0001)
	lo = MAG.readS8(register + 1)
	return  (hi << 8) + lo

readMag(0x03)


for x in range (0,200):
	print "Accl X: ",
	print readAccl(0x28)

	print "Accl Y: ",
	print readAccl(0x2A)
	
	print "Accl Z: ",
	print readAccl(0x2C)
	
	print " "

	print "MAG X: ",
	print readMag(0x03)

	print "MAG Y: ",
	print readMag(0x07)
	
	print "MAG Z: ",
	print readMag(0x05)
	print " "
	time.sleep(.1)

x = raw_input("Press Enter ")



r1 = MAG.write8(LSM303_REGISTER_MAG_MR_REG_M, 0x00)

	
while True:
	print "Accl X: ",
	print readAccl(0x28)

	print "Accl Y: ",
	print readAccl(0x2A)
	
	print "Accl Z: ",
	print readAccl(0x2C)
	
	print " "

	print "MAG X: ",
	print readMag(0x03)

	print "MAG Y: ",
	print readMag(0x07)
	
	print "MAG Z: ",
	print readMag(0x05)
	print " "
	time.sleep(.1)
