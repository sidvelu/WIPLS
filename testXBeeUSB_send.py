import time
import sys
from xbee import XBee
import serial
from digimesh import DigiMesh
import sys

#PORT = '/dev/tty.usbserial-DA017XSD'
PORT = '/dev/tty.usbserial-DA017OQ8'
#PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

if (ser.isOpen()):
    print "its open"

# Create API object
#xbee = XBee(ser, escaped=True)
digi = DigiMesh(ser, escaped=True)

#DEST_ADDR_LONG = b'\x00\x13\xA2\x00\x40\xC4\x04\x84'
DEST_ADDR_LONG = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'
# Continuously read and print packets
while True:
    try:
	print "send data"
#	ser.write("test\n")
	digi.send("tx", dest_addr=DEST_ADDR_LONG, data=sys.argv[1])

#	xbee.send("at", frame='A', command='MY', parameter=None)
#	xbee.at(frame_id='A', command='SH')
##	xbee.send("tx_long_addr", dest_addr=DEST_ADDR_LONG, data='Hello World', id='\x10')
#	xbee.send("tx_long_addr", dest_addr=DEST_ADDR_LONG, data='Hello World')
#	message = "7E 00 0F 10 01 00 00 00 00 00 00 FF FF 00 00 00 00 0D E3"
#	message = "\\x" + message
#	message = message.replace(" ", "\\x")
#	print message
#	ser.write("\x7E\x00\x10\x10\x01\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFE\x00\x00\x7A\x7A\xFF")

#       xbee.tx_long_addr(frame='0x1', dest_addr=DEST_ADDR_LONG, data='AB')
        time.sleep(10)
    except KeyboardInterrupt:
        break

ser.close()

