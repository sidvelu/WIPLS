import time
import math
from Adafruit_I2C import Adafruit_I2C

class MAG3110:

    i2c = None
    xoffset = 0
    yoffset = 0
    zoffset = 0

    def __init__(self, address=0x0e):
        self.i2c = Adafruit_I2C(address) #open up i2c connection
        self.i2c.write8(0x11, 160) #Enable MAG Sensor Resets
        #kself.i2c.write8(0x11, 128) #Enable MAG Sensor Resets
    	time.sleep(.0001)
        self.i2c.write8(0x10, 1)   #Put MAG in active mode, 80HZ ODR

        #Setting up MAG OFFSETS
        # 1.0 / (max - min)
        #self.xoffset = 1.0 / ( 281 - 438 )
        #self.yoffset = 1.0 / ( 38 - 286 )
        #self.zoffset = 1.0 / ( 2070 - 1184 )
    	self.xoffset = 1.0
    	self.yoffset = 1.0
   	self.zoffset = 1.0

    #Reads Mag Values for X, Y, and Z axis
    def magReadX(self):
        register = 0x01
        hi = self.i2c.readS8(register)
        #time.sleep(.0001)
        lo = self.i2c.readU8(register+1)
    	print "S16 X:",
    	print self.i2c.readS16(register)
    	print "S8 X:",
    	print  (hi << 8) + lo
        return (hi << 8) + lo

    def magReadY(self):
        register = 0x03
        hi = self.i2c.readS8(register)
        #time.sleep(.0001)
        lo = self.i2c.readU8(register+1)
    	print "S16 Y:",
    	print self.i2c.readS16(register)
    	print "S8 Y:",
    	print  (hi << 8) + lo
        return (hi << 8) + lo

    def magReadZ(self):
        register = 0x05
        hi = self.i2c.readS8(register)
        #time.sleep(.0001)
        lo = self.i2c.readU8(register+1)
    	print "S16 Z:",
    	print self.i2c.readS16(register)
    	print "S8 Z:",
    	print (hi << 8) + lo
        return (hi << 8) + lo

    def x_out(self):
        return self.magReadX() * self.xoffset
#         return self.magReadX() - ((-541 + 282) / 2.0)

    def y_out(self):
        return self.magReadY() * self.yoffset
#         return self.magReadY() - ((-387 - 43) / 2.0)

    def z_out(self):
        return self.magReadZ() * self.zoffset
#         return self.magReadZ() - ((1295 + 2100) / 2.0)

    def getHeading(self):
        heading = 0.0
	ready = self.i2c.readU8(0x00)
	#print "Ready",
	#print ready

	
	if(ready & 1 == 1 and ready & 2 == 2):
		values = self.i2c.readList(0x01, 6)
		print values
        	X = self.x_out()
        	Y = self.y_out()
		heading  = 180 * math.atan2(Y,X)/math.pi
		if(heading < 0):
			heading = heading + 360

	
	'''
        
        if X == 0 and Y < 0:
            heading = math.pi/2.0

        if X == 0 and Y > 0:
            heading = 3.0 * math.pi/2.0

        if X < 0:
            heading = math.pi - math.atan(Y/X)

        if X > 0 and Y < 0:
            heading = - math.atan(Y/X)

        if X > 0 and Y > 0:
            heading = 2.0 * math.pi - math.atan(Y/X)
	'''
	
        
        '''
    	if Y > 0:
    	    heading = 90 - math.atan(X/Y) * (180/math.pi)
    	if Y < 0:
    	    heading = 270 - math.atan(X/Y) * (180/math.pi)
    	if Y == 0 and X < 0:
    	    heading = 180
    	if Y == 0 and X > 0:
    	    heading = 0
    	'''
        #return math.degrees(heading)
        return heading

