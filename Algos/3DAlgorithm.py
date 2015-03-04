from math import sin, cos, radians, degrees

class Coordinates():
    def __init__(self, X, Y, Z):
        self.x = X
        self.y = Y
        self.z = Z

class BeaconMeasurements():
    def __init__(self, X, Y, Z, phi, theta):
        self.x = X
        self.y = Y
        self.z = Z
        self.phi = radians(phi)
        self.theta = radians(theta)

def triangulate(A, B, C):
    assert isinstance(A, BeaconMeasurements)
    assert isinstance(B, BeaconMeasurements)
    assert isinstance(C, BeaconMeasurements)

    pos1 = getUnknownPosition(A, B)
    print "Corner 1: " + str(pos1.x) + " " + str(pos1.y) + " " + str(pos1.z)
    pos2 = getUnknownPosition(A, C)
    print "Corner 2: " + str(pos2.x) + " " + str(pos2.y) + " " + str(pos2.z)
    pos3 = getUnknownPosition(B, C)
    print "Corner 3: " + str(pos3.x) + " " + str(pos3.y) + " " + str(pos3.z)

    averagePosition = Coordinates((pos1.x + pos2.x + pos3.x)/3, (pos1.y + pos2.y + pos3.y)/3, (pos1.z + pos2.z + pos3.z)/3)

    return averagePosition

def getUnknownPosition(A, B):
    assert isinstance(A, BeaconMeasurements)
    assert isinstance(B, BeaconMeasurements)

    result = Coordinates(None, None, None)

    if (A.theta == B.theta and (A.phi == B.phi or A.phi + radians(180) == B.phi)):
        print "Incompatible angles (same angle or off by 180 degrees)"

    elif (sin(A.phi) * cos(B.phi) * cos(B.theta)) != (cos(A.phi) * sin(B.phi) * cos(B.theta)):
        try:
            #print "Trying XY"

            rB = (cos(A.phi) * (B.y-A.y) - (sin(A.phi) * (B.x-A.x)))/\
                 (cos(B.theta) * (sin(A.phi) * cos(B.phi) - cos(A.phi) * sin(B.phi)))
            rA = (B.x - A.x + cos(B.phi) * cos(B.theta) * rB)/(cos(A.phi) * cos(A.theta))

            result.x = A.x + cos(A.theta)*cos(A.phi) * rA
            result.y = A.y + cos(A.theta)*sin(A.phi) * rA
            result.z = A.z + sin(A.theta) * rA

        except ZeroDivisionError:
            print "XY: Division by Zero"

    elif cos(B.phi) * cos(B.theta) * sin(A.theta) != cos(A.phi) * cos(A.theta) * sin(B.theta):
        try:
            #print "Trying XZ"

            rB = ((cos(A.phi) * cos(A.theta)) * (B.z-A.z) - sin(A.theta) * (B.x-A.x))/\
                (cos(B.phi) * cos(B.theta) * sin(A.theta) - cos(A.phi) * cos(A.theta) * sin(B.theta))
            rA = (B.x - A.x + cos(B.phi) * cos(B.theta) * rB)/(cos(A.phi) * cos(A.theta))

            result.x = A.x + cos(A.theta)*cos(A.phi) * rA
            result.y = A.y + cos(A.theta)*sin(A.phi) * rA
            result.z = A.z + sin(A.theta) * rA
    
        except:
            print "XZ: Division by Zero"

    elif sin(A.theta) * sin(B.phi) * cos(B.theta) != sin(A.phi) * cos(A.theta) * sin(B.theta):
        try:
            #print "Trying YZ"

            rB = ((sin(A.phi) * cos(A.theta)) * (B.z-A.z) - sin(A.theta) * (B.y-A.y))/\
                 (sin(A.theta) * sin(B.phi) * cos(B.theta) - sin(A.phi) * cos(A.theta) * sin(B.theta))
            rA = (B.z - A.z + sin(B.theta) * rB)/sin(A.theta)

            result.x = A.x + cos(A.theta)*cos(A.phi) * rA
            result.y = A.y + cos(A.theta)*sin(A.phi) * rA
            result.z = A.z + sin(A.theta) * rA

            print rA, rB, result.x, result.y, result.z

        except ZeroDivisionError:
            print "YZ: Division by Zero"

    else:
        print "Fell through all cases: investigate"

    return result

# Triangulate

# Enter info here
Beacon1lat = 42.337435
Beacon1long = -71.091525
Beacon1angle = 175

Beacon2lat = 42.33765
Beacon2long = -71.08964333333333
Beacon2angle = 254

Beacon3lat = 42.33734
Beacon3long = -71.09050666666667
Beacon3angle = 190

# Don't edit this part
Beacon1x = Beacon1lat
Beacon1y = Beacon1long
Beacon1z = 0
Beacon1phi = Beacon1angle
Beacon1theta = 0

Beacon2x = Beacon2lat
Beacon2y = Beacon2long
Beacon2z = 0
Beacon2phi = Beacon2angle
Beacon2theta = 0

Beacon3x = Beacon3lat
Beacon3y = Beacon3long
Beacon3z = 0
Beacon3phi = Beacon3angle
Beacon3theta = 0

tracker1 = BeaconMeasurements(Beacon1x, Beacon1y, Beacon1z, Beacon1phi, Beacon1theta)
tracker2 = BeaconMeasurements(Beacon2x, Beacon2y, Beacon2z, Beacon2phi, Beacon2theta)
tracker3 = BeaconMeasurements(Beacon3x, Beacon3y, Beacon3z, Beacon3phi, Beacon3theta)

answer = triangulate(tracker1, tracker2, tracker3)
print "Guess: " + str(answer.x) + ", " + str(answer.y) + ", " + str(answer.z) + "\n"

# Findunknownposition test case
# Solution is at 0, 1, 2
# One tracker at 1, 1, 1 with phi 180 and theta 45 (45degrees between -x and +z)
# Other tracker at 0, 2, 1 with phi 270 and theta 45 (45degrees between -y and +z)

# phi should be in [0, 360)
# theta should be in [0, 90] (realistically it won't reach 90 because of our pan/tilt limitations)

Beacon1x = 1
Beacon1y = 1
Beacon1z = 1
Beacon1phi = 180
Beacon1theta = 45

Beacon2x = 0
Beacon2y = 2
Beacon2z = 1
Beacon2phi = 270
Beacon2theta = 45

a_measure = BeaconMeasurements(Beacon1x, Beacon1y, Beacon1z, Beacon1phi, Beacon1theta)
b_measure = BeaconMeasurements(Beacon2x, Beacon2y, Beacon2z, Beacon2phi, Beacon2theta)

print "Beacon 1 coordinates: " + str(Beacon1x) + ", " + str(Beacon1y) + ", " + str(Beacon1z)
print "Beacon 1 measurements: Phi (x/y): " + str(Beacon1phi) + ", Theta (xy/z): " + str(Beacon1theta)
print "Beacon 2 coordinates: " + str(Beacon2x) + ", " + str(Beacon2y) + ", " + str(Beacon2z)
print "Beacon 2 measurements: Phi (x/y): " + str(Beacon2phi) + ", Theta (xy/z): " + str(Beacon2theta)

ans = getUnknownPosition(a_measure, b_measure)
print "Solution coordinates: " + str(ans.x) + ", " + str(ans.y) + ", " + str(ans.z)

print ""
testnumber = 0

# Tests
testnumber += 1
a_measure = BeaconMeasurements(0, 0, 0, 0, 0)
b_measure = BeaconMeasurements(1, 1, 0, 270, 0)
true_coordinates = Coordinates(1, 0, 0)
coordinates = getUnknownPosition(a_measure, b_measure)
print "Test " + str(testnumber) + ": " + str(coordinates.x) + ", " + str(coordinates.y) + ", " + str(coordinates.z)
assert abs(coordinates.x - true_coordinates.x) < .0001
assert abs(coordinates.y - true_coordinates.y) < .0001
assert abs(coordinates.z - true_coordinates.z) < .0001

testnumber += 1
a_measure = BeaconMeasurements(0, 0, 0, 0, 0)
b_measure = BeaconMeasurements(5, 0, 0, 180, 0)
true_coordinates = Coordinates(None, None, None)
coordinates = getUnknownPosition(a_measure, b_measure)
print "Test " + str(testnumber) + ": " + str(coordinates.x) + ", " + str(coordinates.y) + ", " + str(coordinates.z)
assert coordinates.x is None
assert coordinates.y is None
assert coordinates.z is None

testnumber += 1
a_measure = BeaconMeasurements(1, 1, 1, 180, 45)
b_measure = BeaconMeasurements(0, 2, 1, 270, 45)
true_coordinates = Coordinates(0, 1, 2)
coordinates = getUnknownPosition(a_measure, b_measure)
print "Test " + str(testnumber) + ": " + str(coordinates.x) + ", " + str(coordinates.y) + ", " + str(coordinates.z)
assert abs(coordinates.x - true_coordinates.x) < .0001
assert abs(coordinates.y - true_coordinates.y) < .0001
assert abs(coordinates.z - true_coordinates.z) < .0001