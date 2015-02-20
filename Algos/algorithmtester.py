from math import sin, cos, radians, degrees

f = open('invalid.txt', 'w')
f.write("Invalid combinations:\n")
f.write("phiA | phiB | thetaA | thetaB\n")

for phiAdeg in range(0,359):
    print phiAdeg
    phiA = radians(phiAdeg)
    for phiBdeg in range(0,359):
        phiB = radians(phiBdeg)
        for thetaAdeg in range(0,89):
            thetaA = radians(thetaAdeg)
            for thetaBdeg in range(0,89):
                thetaB = radians(thetaBdeg)
                fails = 0
                if sin(thetaA)*sin(phiB)*cos(thetaB) == sin(phiA)*cos(thetaA)*sin(thetaB):
                    #print "Y/Z equation fails for " + str(phiA) + ", " + str(phiB) + ", " + str(thetaA) + ", " + str(thetaB)
                    fails += 1
                if cos(phiB)*cos(thetaB)*sin(thetaA) == cos(phiA)*cos(thetaA)*sin(thetaB):
                    #print "X/Z equation fails for " + str(phiA) + ", " + str(phiB) + ", " + str(thetaA) + ", " + str(thetaB)
                    fails += 1
                if sin(phiA)*cos(phiB) == cos(phiA)*sin(phiB):
                    #print "X/Y equation fails for " + str(phiA) + ", " + str(phiB) + ", " + str(thetaA) + ", " + str(thetaB)
                    fails += 1
                if fails == 3:
                    if phiA == phiB and thetaA == thetaB:
                        #print "Same line"
                        x = 0
                    else:
                        print "FAILS ALL EQNS :("
                        f.write(str(degrees(phiA)) + ", " + str(degrees(phiB)) + ", " + str(degrees(thetaA)) + ", " + str(degrees(thetaB)) + "\n")
                        print str(degrees(phiA)) + ", " + str(degrees(phiB)) + ", " + str(degrees(thetaA)) + ", " + str(degrees(thetaB))
                        #f.write(str(degrees(phiA)) + ", " + str(degrees(phiB)) + ", " + str(degrees(thetaA)) + ", " + str(degrees(thetaB)))
