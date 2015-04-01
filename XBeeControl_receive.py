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

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = digi.wait_read_frame()
        if (response['data'] != ""):
            rawData = open('Map/fakeinput.txt', 'w') # clear it
            rawData.write(response['data'])
            rawData.close()
            execfile('Map/JSONWriteTest.py')  # will block till done
	    print response['data']
    except KeyboardInterrupt:
        rawData.close()
        break

rawData.close()
ser.close()
