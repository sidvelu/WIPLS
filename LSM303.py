import time
import math
from Adafruit_I2C import Adafruit_I2C

class LSM303:

    MAG = None
    ACCL = None
    xoffset = 0
    yoffset = 0
    zoffset = 0

    def __init__(self):
        self.ACCL = Adafruit_I2C(0x32 >> 1) #open up MAG
        self.MAG = Adafruit_I2C(0x3C >> 1) # Open up ACCL

        self.ACCL.write8(0x20, 0x27) # Turn Accl On
        self.MAG.write8(0x02, 0x00)  # Turn Mag On
        self.MAG.write8(0x01, 0x60)  # +- 2.5 Gauss

        #Setting up MAG OFFSETS
        self.xoffset = (229  - 206) / 2
        self.yoffset = (98 - 96) / 2
        self.zoffset = (-255 - 405) / 2

    #Reads Mag Values for X, Y, and Z axis
    def magReadX(self):
        register = 0x03
        hi = self.MAG.readS8(register)
        time.sleep(.0001)
        lo = self.MAG.readU8(register + 1)
        return (hi << 8) + lo - self.xoffset

    def magReadY(self):
        register = 0x07
        hi = self.MAG.readS8(register)
        time.sleep(.0001)
        lo = self.MAG.readU8(register + 1)
        return  (hi << 8) + lo - self.yoffset

    def magReadZ(self):
        register = 0x05
        hi = self.MAG.readS8(register)
        time.sleep(.0001)
        lo = self.MAG.readU8(register + 1)
        return  (hi << 8) + lo - self.zoffset


    def readAcclX(self):
        register = 0x28
        lo = self.ACCL.readU8(register)
        time.sleep(.0001)
        hi = self.ACCL.readS8(register + 1)
        return  ((hi << 8) + lo) >> 4

    def readAcclY(self):
        register = 0x2A
        lo = self.ACCL.readU8(register)
        time.sleep(.0001)
        hi = self.ACCL.readS8(register + 1)
        return  ((hi << 8) + lo) >> 4

    def readAcclZ(self):
        register = 0x2C
        lo = self.ACCL.readU8(register)
        time.sleep(.0001)
        hi = self.ACCL.readS8(register + 1)
        return  ((hi << 8) + lo) >> 4

    def getHeading(self):
        magX = self.magReadX()
        magY = self.magReadY()
        magZ = self.magReadZ()

        acclX = self.readAcclX()
        acclY = self.readAcclY()
        acclZ = self.readAcclZ()

        normX = math.atan( acclX /   math.sqrt(acclX * acclX + acclY * acclY +  acclZ * acclZ) )
        pitch = math.asin(-normX)

        normY = math.atan( acclY /   math.sqrt(acclX * acclX + acclY * acclY +  acclZ * acclZ) )
        roll = math.asin(normY/math.cos(pitch))

        xH2 = magX * math.cos(pitch) + magZ * math.sin(pitch)
        yH2 = magX * math.sin(roll) * math.sin(pitch) + magY * math.cos(roll) - magZ * math.sin(roll) * math.cos(pitch)
        heading = 180 * math.atan2(yH2, xH2) / math.pi
        if heading < 0:
            heading  = heading + 360

        return heading

