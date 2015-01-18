from LSM303 import LSM303
import time

try:
    compass = LSM303()
    print "Compass Active"
except:
    print "Error Activating Compass"

Xmax = 0
Xmin = 0
Ymax = 0
Ymin = 0
Zmax = 0
Zmin = 0

for i in range (0,200):
	X =  compass.magReadX()
	Y =  compass.magReadY()
	Z =  compass.magReadZ()
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

	

