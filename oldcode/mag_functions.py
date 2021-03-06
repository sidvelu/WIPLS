import time
from Adafruit_I2C import Adafruit_I2C

class MAG3110:

	i2c = None

	def __init__(self, address=0x0e):
		self.i2c = Adafruit_I2C(address)
		self.i2c.write8(0x11, 128)
		self.i2c.write8(0x10, 1)

	#Reads Mag Values for X, Y, and Z axis
	def magRead(self, Axis):
		if Axis == 'X':
			register = 0x01
		if Axis == 'Y':
			register = 0x03	
		if Axis == "Z":
			register = 0x05

		hi = self.i2c.readS8(register)
		lo = self.i2c.readU8(register+1)
		return (hi << 8) + lo
