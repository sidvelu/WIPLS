from math import sin, cos

class Coordinates():
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

class BeaconMeasurements():
    def __init__(self, X, Y, theta):
        self.x = X
        self.y = Y
        self.theta = theta

def getUnknownPosition(A, B):
    assert isinstance(A, BeaconMeasurements)
    assert isinstance(B, BeaconMeasurements)

    result = Coordinates(None, None)

    try:
        rB = (sin(A.theta)*(A.x-B.x) + cos(A.theta) * (B.y-A.y)) / ((sin(A.theta)*cos(B.theta))-(cos(A.theta)*sin(B.theta)))
        rA = (B.x + cos(B.theta) * rB - A.x)/cos(A.theta)

        result.x = A.x + cos(A.theta) * rA
        result.y = A.y + sin(A.theta) * rA
    except ZeroDivisionError:
        try:
            print "Try 1: Division by Zero"
            rA = (sin(B.theta)*(B.x-A.x) + cos(B.theta) * (A.y-B.y)) / ((sin(B.theta)*cos(A.theta))-(cos(B.theta)*sin(A.theta)))
            rB = (A.x + cos(A.theta) * rA - B.x)/cos(B.theta)

            result.x = A.x + cos(A.theta) * rA
            result.y = A.y + sin(A.theta) * rA
            
        except ZeroDivisionError:
            print "Try 2: Division by Zero"

    return result

a_measure = BeaconMeasurements(0, 0, 1)
b_measure = BeaconMeasurements(20, 10, -1)

ans = getUnknownPosition(a_measure, b_measure)
print ans.x, ans.y

#http://www.wolframalpha.com/input/?i=0+%3D+sin%28A%29cos%28B%29-%28cos%28A%29*sin%28B%29%29