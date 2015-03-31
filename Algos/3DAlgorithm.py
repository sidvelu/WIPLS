from math import sin, cos, tan, radians, degrees
import utm

class Coordinates():
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

class GPSCoordinates():
    def __init__(self, lat, long, height):
        self.lat = lat
        self.long = long
        self.height = height
    def printCoordinates(self):
        print "(" + str(self.lat) + ", " + str(self.long) + ") @ " + str(self.height)

class BeaconMeasurements():
    def __init__(self, X, Y, Z, phi, theta):
        self.x = X
        self.y = Y
        self.z = Z
        self.phi = radians(phi)
        self.theta = radians(theta)

def outputJSON(A, B, C, ans):
    print '\t"beaconGuessCoords": {'
    print '\t\t"lat": ' + str(ans.lat) + ','
    print '\t\t"long": ' + str(ans.long) + ','
    print '\t\t"ele": ' + str(ans.height)
    print '\t},'

    print '\t"guessVector": ['
    print '\t\t{'
    print '\t\t\t"lat": ' + str(A.x) + ','
    print '\t\t\t"long": ' + str(A.y) + ','
    print '\t\t\t"ele": ' + str(A.z)
    print '\t\t},'
    print '\t\t{'
    print '\t\t\t"lat": ' + str(B.x) + ','
    print '\t\t\t"long": ' + str(B.y) + ','
    print '\t\t\t"ele": ' + str(B.z)
    print '\t\t},'
    print '\t\t{'
    print '\t\t\t"lat": ' + str(C.x) + ','
    print '\t\t\t"long": ' + str(C.y) + ','
    print '\t\t\t"ele": ' + str(C.z)
    print '\t\t}'
    print '\t]'

def start(lat1, long1, he1, phi1, theta1, lat2, long2, he2, phi2, theta2, lat3, long3, he3, phi3, theta3):
    lat1 = float(lat1)
    long1 = float(long1)
    he1 = float(he1)
    phi1 = float(phi1)
    theta1 = float(theta1)
    lat2 = float(lat2)
    long2 = float(long2)
    he2 = float(he2)
    phi2 = float(phi2)
    theta2 = float(theta2)
    lat3 = float(lat3)
    long3 = float(long3)
    he3 = float(he3)
    phi3 = float(phi3)
    theta3 = float(theta3)


    GPS1 = GPSCoordinates(lat1, long1, he1)
    GPS2 = GPSCoordinates(lat2, long2, he2)
    GPS3 = GPSCoordinates(lat3, long3, he3)

    Bea1 = BeaconMeasurements(GPS1.long, GPS1.lat, GPS1.height, phi1, theta1)
    Bea2 = BeaconMeasurements(GPS2.long, GPS2.lat, GPS2.height, phi2, theta2)
    Bea3 = BeaconMeasurements(GPS3.long, GPS3.lat, GPS3.height, phi3, theta3)

    #print "getUnknownPosition A,B"
    pos1 = getUnknownPosition(Bea1, Bea2)
    print "Corner 1: " + str(pos1.x) + " " + str(pos1.y) + " " + str(pos1.z)

    #print "getUnknownPosition C,A"
    pos2 = getUnknownPosition(Bea3, Bea1)
    print "Corner 2: " + str(pos2.x) + " " + str(pos2.y) + " " + str(pos2.z)

    #print "getUnknownPosition B,C"
    pos3 = getUnknownPosition(Bea2, Bea3)
    print "Corner 3: " + str(pos3.x) + " " + str(pos3.y) + " " + str(pos3.z)

    averagePosition = GPSCoordinates((pos1.x + pos2.x + pos3.x)/3.0, (pos1.y + pos2.y + pos3.y)/3.0, (pos1.z + pos2.z + pos3.z)/3.0)

    outputJSON(pos1, pos2, pos3, averagePosition)

    return averagePosition

def getUnknownPosition(A, B):
    assert isinstance(A, BeaconMeasurements)
    assert isinstance(B, BeaconMeasurements)

    result = Coordinates(None, None, None)

    if (A.theta == B.theta and (A.phi == B.phi or A.phi + radians(180) == B.phi)):
        print "Incompatible angles (same angle or off by 180 degrees)"

    dB = (cos(A.phi)*(B.y-A.y)-sin(A.phi)*(B.x-A.x)) / (sin(A.phi) * cos(B.phi) - sin(B.phi) * cos(A.phi))
    dA = (B.x - A.x + cos(B.phi) * dB) / cos(A.phi)

    result.y = A.x + cos(A.phi) * dA
    result.x = A.y + sin(A.phi) * dA
    result.z = (dA * tan(A.theta) + dB * tan(B.theta)) / 2.0

    return result

# Flagpole
# start(42.337435,-71.091525,0,175,0,
#      42.33765,-71.089643333333,0,254,0,
#      42.33734,-71.09050666667,0,190,0)

# DDs
# start(42.337485,-71.09112833333333,0,190,0,
#     42.337536666666665,-71.089375,0,270,0,
#     42.33830833333333,-71.08997166666667,0,203,0)

# Ideal data
start(42.337545,-71.089335,0.0,203.0,0.0,
      42.337414,-71.090456,0.0,265.0,0.0,
      42.336946,-71.091264,0.0,12.0,0.0)