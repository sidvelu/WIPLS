__author__ = 'siddharth'

from MAG3110 import MAG3110
import time

try:
	mag = MAG3110()
	print "I2C Bus is accessible"
except:
	print "Error in opening up I2C Bus"


Xmax = 0
Xmin = 0
Ymax = 0
Ymin = 0
Zmax = 0
Zmin = 0

for i in range (0,200):
    X = mag.magReadX()
    Y = mag.magReadY()
    Z = mag.magReadZ()
    if i == 0 :
        Xmax = X
        Xmin = X
        Ymax = Y
        Ymin = Y
        Zmax = Z
        Zmin = Z
    if X > Xmax:
        Xmax = X
    if X < Xmin:
        Xmin = X
    if Y > Ymax:
        Ymax = Y
    if Z > Zmax:
        Zmax = Z
    if Z < Zmin:
        Zmin = Z

    print "X :" + str(X)
    print "Y :" + str(Y)
    print "Z :" + str(Z)
    print ""
    time.sleep(.1)

print "Xmax :" + str(Xmax)
print "Xmin :" + str(Xmin)
print "Ymax :" + str(Ymax)
print "Ymin :" + str(Ymin)
print "Zmax :" + str(Zmax)
print "Zmin :" + str(Zmin)
