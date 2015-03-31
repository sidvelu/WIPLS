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

    def toUTM(self):
        easting, northing, zonenum, zonelet = utm.from_latlon(self.lat,self.long)
        utmc = UTMCoordinates(easting, northing, zonenum, zonelet, self.height)
        return utmc

class UTMCoordinates():
    def __init__(self, easting, northing, zonenum, zonelet, height):
        self.easting = easting
        self.northing = northing
        self.zonenum = zonenum
        self.zonelet = zonelet
        self.height = height
    def printCoordinates(self):
        print "(" + str(self.easting) + ", " + str(self.northing) + ", " + str(self.zonenum) \
              + ", " + str(self.zonelet) + ") @ " + str(self.height)
    def toGPS(self):
        lat, long = utm.to_latlon(self.easting, self.northing, self.zonenum, self.zonelet)
        gps = GPSCoordinates(lat, long, self.height)
        return gps

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
    print '\t\t\t"lat": ' + str(A.lat) + ','
    print '\t\t\t"long": ' + str(A.long) + ','
    print '\t\t\t"ele": ' + str(A.height)
    print '\t\t},'
    print '\t\t{'
    print '\t\t\t"lat": ' + str(B.lat) + ','
    print '\t\t\t"long": ' + str(B.long) + ','
    print '\t\t\t"ele": ' + str(B.height)
    print '\t\t},'
    print '\t\t{'
    print '\t\t\t"lat": ' + str(C.lat) + ','
    print '\t\t\t"long": ' + str(C.long) + ','
    print '\t\t\t"ele": ' + str(C.height)
    print '\t\t}'
    print '\t]'

def start(lat1, long1, he1, phi1, theta1, lat2, long2, he2, phi2, theta2, lat3, long3, he3, phi3, theta3):
    GPS1 = GPSCoordinates(lat1, long1, he1)
    GPS2 = GPSCoordinates(lat2, long2, he2)
    GPS3 = GPSCoordinates(lat3, long3, he3)
    UTM1 = GPS1.toUTM()
    UTM2 = GPS2.toUTM()
    UTM3 = GPS3.toUTM()
    Bea1 = BeaconMeasurements(UTM1.easting, UTM1.northing, UTM1.height, phi1, theta1)
    Bea2 = BeaconMeasurements(UTM2.easting, UTM2.northing, UTM2.height, phi2, theta2)
    Bea3 = BeaconMeasurements(UTM3.easting, UTM3.northing, UTM3.height, phi3, theta3)

    max = 9999999.0
    min = 0.0

    #print "getUnknownPosition A,B"
    pos1 = getUnknownPosition(Bea1, Bea2)
    print "Corner 1: " + str(pos1.x) + " " + str(pos1.y) + " " + str(pos1.z)

    if pos1.x > max or pos1.x < min or pos1.y > max or pos1.y < min or pos1.z > max or pos1.z < min:

        pos1 = getUnknownPosition(Bea2, Bea1)
        print "Corner 1: " + str(pos1.x) + " " + str(pos1.y) + " " + str(pos1.z)


    #print "getUnknownPosition C,A"
    pos2 = getUnknownPosition(Bea3, Bea1)
    print "Corner 2: " + str(pos2.x) + " " + str(pos2.y) + " " + str(pos2.z)

    if pos2.x > max or pos2.x < min or pos2.y > max or pos2.y < min or pos2.z > max or pos2.z < min:

        pos2 = getUnknownPosition(Bea1, Bea3)
        print "Corner 2: " + str(pos2.x) + " " + str(pos2.y) + " " + str(pos2.z)


    #print "getUnknownPosition B,C"
    pos3 = getUnknownPosition(Bea2, Bea3)
    print "Corner 3: " + str(pos3.x) + " " + str(pos3.y) + " " + str(pos3.z)

    if pos3.x > max or pos3.x < min or pos3.y > max or pos3.y < min or pos3.z > max or pos3.z < min:

        pos3 = getUnknownPosition(Bea3, Bea2)
        print "Corner 3: " + str(pos3.x) + " " + str(pos3.y) + " " + str(pos3.z)


    averagePosition = Coordinates((pos1.x + pos2.x + pos3.x)/3, (pos1.y + pos2.y + pos3.y)/3, (pos1.z + pos2.z + pos3.z)/3)

    UTM1f = UTMCoordinates(pos1.x, pos1.y, UTM1.zonenum, UTM1.zonelet, pos1.z)
    UTM2f = UTMCoordinates(pos2.x, pos2.y, UTM2.zonenum, UTM2.zonelet, pos2.z)
    UTM3f = UTMCoordinates(pos3.x, pos3.y, UTM3.zonenum, UTM3.zonelet, pos3.z)
    UTMAvg = UTMCoordinates(averagePosition.x, averagePosition.y, UTM1.zonenum, UTM1.zonelet, averagePosition.z)
    GPS1f = UTM1f.toGPS()
    GPS2f = UTM2f.toGPS()
    GPS3f = UTM3f.toGPS()
    GPSAvg = UTMAvg.toGPS()

    outputJSON(GPS1f, GPS2f, GPS3f, GPSAvg)

    return averagePosition

def getUnknownPosition(A, B):
    assert isinstance(A, BeaconMeasurements)
    assert isinstance(B, BeaconMeasurements)

    result = Coordinates(None, None, None)

    if (A.theta == B.theta and (A.phi == B.phi or A.phi + radians(180) == B.phi)):
        print "Incompatible angles (same angle or off by 180 degrees)"

    dB = (cos(A.phi)*(B.y-A.y)-sin(A.phi)*(B.x-A.x)) /\
         sin(A.phi) * cos(B.phi) - sin(B.phi) * cos(A.phi)
    dA = (B.x - A.x + cos(B.phi) * dB) / cos(A.phi)

    result.x = A.x + cos(A.phi) * dA
    result.y = A.y + sin(A.phi) * dA
    result.z = (dA * tan(A.theta) + dB * tan(B.theta)) / 2

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
start(42.337545,-71.089335,0,215,0,
      42.337414,-71.090456,0,265,0,
      42.336946,-71.091264,0,15,0)