import time
from xbee import XBee
import serial
from digimesh import DigiMesh
import sys

#PORT = '/dev/tty.usbserial-DA017XSD'
PORT = '/dev/ttyUSB0'
#PORT = '/dev/tty.usbserial-DA017OQ8'
BAUD_RATE = 9600

if(len(sys.argv) <= 1):
    print "Error: Please Enter Command"
    exit()

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

if (not ser.isOpen()):
    print "ERROR"

# Create API object
#xbee = XBee(ser, escaped=True)
digi = DigiMesh(ser, escaped=True)

#DEST_ADDR_LONG = b'\x00\x13\xA2\x00\x40\xC4\x04\x84'
DEST_ADDR_LONG = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'

# Continuously read and print packets
try:
    #print "send data ", sys.argv[1]
	digi.send("tx", dest_addr=DEST_ADDR_LONG, data=sys.argv[1])

except KeyboardInterrupt:
    print "error"

ser.close()

