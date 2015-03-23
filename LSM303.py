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

        #self.ACCL.write8(0x23, 0x08)
        #self.ACCL.write8(0x20, 0x47)
        #self.MAG.write8(0x00, 0x0C)
        #self.MAG.write8(0x01, 0x20)
        #self.MAG.write8(0x02, 0x00)

        #Setting up MAG OFFSETS
        # fomrula: (min + max)/2.0
        #self.xoffset = (-247 + 319) / 2
        #self.yoffset = (-142 + 213) / 2
        #self.zoffset = (-5 + 482) / 2

        # original
        #self.xoffset = (229 - 206) / 2
        #self.yoffset = (98 - 96) / 2
        #self.zoffset = (-255 - 405) / 2

        # new
        self.xoffset = (-435 + 586) / 2
        self.yoffset = (-351 + 491) / 2
        self.zoffset = (-263 + 648) / 2

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

    def cross(self, a, b):
        out = list()
        out.append((a[1] * b[2]) - (a[2] * b[1]))
        out.append((a[2] * b[0]) - (a[0] * b[2]))
        out.append((a[0] * b[1]) -(a[1] * b[0]))
        return out

    def dot(self, a, b):
        return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])

    def normalize(self, a):
        mag = math.sqrt(self.dot(a, a))
        a[0] /= mag
        a[1] /= mag
        a[2] /= mag
        return a

    def getPitch(self):
        acclX = self.readAcclX()
        acclY = self.readAcclY()
        acclZ = self.readAcclZ()

        normX = math.atan( acclX /   math.sqrt(acclX * acclX + acclY * acclY +  acclZ * acclZ) )
        pitch = math.asin(-normX)
        return pitch
        

    def getHeading(self, offset=False):
        if offset == True:
            magX = self.magReadX() - self.xoffset
            magY = self.magReadY() - self.yoffset
            magZ = self.magReadZ() - self.zoffset
        elif offset == False:
            magX = self.magReadX()
            magY = self.magReadY()
            magZ = self.magReadZ()

        acclX = self.readAcclX()
        acclY = self.readAcclY()
        acclZ = self.readAcclZ()

        # new technique, gave same results
        '''
        m = list()
        a = list()
        m.extend((magX, magY, magZ))
        a.extend((acclX, acclY, acclZ))
        
        E = self.cross(m, a)
        E = self.normalize(E)
        N = self.cross(a, E)
        N = self.normalize(N)

        fromz = list()
        fromz.extend((0, -1, 0))

        heading = math.atan2(self.dot(E, fromz), self.dot(N, fromz)) * 180 / math.pi

        '''
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

