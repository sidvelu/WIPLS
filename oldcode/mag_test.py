from Adafruit_I2C import Adafruit_I2C
import time

#i2c = Adafruit_I2C("0x4802A000")
try:
	i2c = Adafruit_I2C(0x0e)
	print "Default I2C bus is accessible"
except:
	print "Error accessing default I2C bus"

print "test"

#try:
def dectobin( number, index ):
	if index == 16:
		print ""
	else:
		X = 1&number,
		number = number >> 1	
		dectobin(number, index+1)
		print str(X),


	

#i2c.write8(0x16, 1)
X_OUT = i2c.readU16(0x01)
print X_OUT
Y_OUT = i2c.readU16(0x03)
print Y_OUT
WHO = i2c.readU16(0x07)
print WHO
MODE = i2c.readU16(0x08)
print MODE

CTRL2 = i2c.readU8(0x11)
print CTRL2

i2c.write8(0x11, 128)
i2c.write8(0x10, 1)


while True:
	X = i2c.readS16(0x01)
	#print "X bit length " + str(X.bit_length())
	#dectobin(X,0)
	X2 = i2c.readS16(0x02)
	#print "X2 bit length " + str(X2.bit_length())
	X = X | X2
	print "X Value: " + str(X)
	#print "X2 Value: " + str(X2)
	
		
	#print "X components: " + bin(i2c.readS8(0x01)) + " " + bin(i2c.readS8(0x02))

	Y = i2c.readS16(0x03)
	#Y = Y << 8
	Y2 = i2c.readS16(0x04)
	Y = Y | Y2
	print "Y Value: " + str(Y)
	
	#print "Y components: " + str(i2c.readU16(0x03)) + " " + str(i2c.readU16(0x04))
	
	Z = i2c.readS16(0x05)
	Z = Z << 8
	Z2 = i2c.readS16(0x06)
	Z = Z | Z2
	print "Z Value: " + str(Z)
	
	
	#print "Z components: " + str(i2c.readU16(0x05)) + " " + str(i2c.readU16(0x06))

	print ""
	time.sleep(.9)
