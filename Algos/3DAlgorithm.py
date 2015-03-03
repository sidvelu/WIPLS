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

# Test case
# Solution is at 0, 1, 2
# One tracker at 1, 1, 1 with phi 180 and theta 45 (45degrees between -x and +z)
# Other tracker at 0, 2, 1 with phi 270 and theta 45 (45degrees between -y and +z)

# phi should be in [0, 360)
# theta should be in [0, 90] (realistically it won't reach 90 because of our pan/tilt limitations)

Beacon1x = -71.08964333333333
Beacon1y = 42.33765
Beacon1z = 0
Beacon1phi = 254
Beacon1theta = 0

Beacon2x = -71.09050666666667
Beacon2y = 42.33734
Beacon2z = 0
Beacon2phi = 190
Beacon2theta = 0

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