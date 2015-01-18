import time
import math
import os
from Adafruit_I2C import Adafruit_I2C


# I2C address constants
os.system('i2cdetect -y -r 1')
ACCL = Adafruit_I2C(0x32 >> 1) # 1B
MAG = Adafruit_I2C(0x3C >> 1)  # 1E

# MAG register constants
LSM303_REGISTER_MAG_CRA_REG_M = 0x00
LSM303_REGISTER_MAG_CRB_REG_M = 0x01
LSM303_REGISTER_MAG_MR_REG_M = 0x02

print str(hex(MAG.address))
ACCL.write8(0x20, 0x27)
os.system('i2cdetect -y -r 1')
time.sleep(.00001)
while True:
	try:
		r1 = MAG.write8(LSM303_REGISTER_MAG_MR_REG_M, 0x00)
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
	return  ((hi << 8) + lo) >> 4


def readMag( register):
	hi = MAG.readS8(register)
	time.sleep(.0001)
	lo = MAG.readU8(register + 1)
	return  (hi << 8) + lo

readMag(0x03)

def getHeading(magX, magY):
	heading = 180 * math.atan2(magY, magX) / math.pi
	if heading < 0:
		heading  = heading + 360
	return heading

def getTiltHeading(magX, magY, magZ, acclX, acclY, acclZ):
	#pitch = math.atan( acclX /   math.sqrt(acclY * acclY +  acclZ * acclZ) )
	normX = math.atan( acclX /   math.sqrt(acclX * acclX + acclY * acclY +  acclZ * acclZ) )
	pitch2 = math.asin(-normX)
	#print "Pitch: " + str(pitch)
	#print "PitchNorm: " + str(pitch2)

	#roll = math.atan( acclY /   math.sqrt(acclX * acclX +  acclZ * acclZ) )
	normY = math.atan( acclY /   math.sqrt(acclX * acclX + acclY * acclY +  acclZ * acclZ) )
	roll2 = math.asin(normY/math.cos(pitch2))
	#print "ROll: " + str(roll)
	#print "Roll Norm: " + str(roll2)


	#xH = magX * math.cos(pitch) + magZ * math.sin(pitch)
	#yH = magX * math.sin(roll) * math.sin(pitch) + magY * math.cos(roll) - magZ * math.sin(roll) * math.cos(pitch)

	xH2 = magX * math.cos(pitch2) + magZ * math.sin(pitch2)
	yH2 = magX * math.sin(roll2) * math.sin(pitch2) + magY * math.cos(roll2) - magZ * math.sin(roll2) * math.cos(pitch2)
	heading2 = 180 * math.atan2(yH2, xH2) / math.pi
	if heading2 < 0:
		heading2  = heading2 + 360
	#print "Heading2: " + str(heading2)
	'''

	heading = 180 * math.atan2(yH, xH) / math.pi
	if heading < 0:
		heading  = heading + 360
	'''

	return heading2

while True:
	print "Accl X: ",
	acclX = readAccl(0x28)
	print acclX

	print "Accl Y: ",
	acclY = readAccl(0x2A)
	print acclY
	
	print "Accl Z: ",
	acclZ = readAccl(0x2C)
	print acclZ
	
	print " "

	print "MAG X: ",
	magX =  readMag(0x03)
	print magX

	print "MAG Y: ",
	magY = readMag(0x07)
	print magY
	
	print "MAG Z: ",
	magZ = readMag(0x05)
	print magZ

	print "Heading: ",
	print getHeading(magX, magY)

	print "Tilt Heading : ",
	print getTiltHeading(magX, magY, magZ, acclX, acclY, acclZ)

	print " "
	time.sleep(.1)



	
