from xbee import XBee
import serial
from digimesh import DigiMesh
import sys

if "linux" in sys.platform:
    PORT = '/dev/ttyUSB0'
elif "darwin" in sys.platform:
    #PORT = '/dev/tty.usbserial-DA017XSD'
    PORT = '/dev/tty.usbserial-DA017OQ8'

BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

if (ser.isOpen()):
    print "its open"

# Create API object
#xbee = XBee(ser, escaped=True)
digi = DigiMesh(ser, escaped=True)

t1, t2, t3 = 0 , 0 , 0

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = digi.wait_read_frame()
        response = response['data'].split()
        print response
        if "mag" in response[1]:
            if "1" in response[0]:
                t1 = float(response[2])
            elif "2" in response[0]:
                t2 = float(response[2])
            elif "3" in response[0]:
                t3 = float(response[2])
        print "t1:" + str(t1) + " t2:" + str(t2) +" t3:" + str(t3)

    except KeyboardInterrupt:
        rawData.close()
        break

rawData.close()
ser.close()
