from xbee import XBee
import serial
from digimesh import DigiMesh

PORT = '/dev/tty.usbserial-DA017OQ8'
#PORT = '/dev/tty.usbserial-DA017XSD'
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
#        response = xbee.wait_read_frame()
	response = digi.wait_read_frame()
##	response = ser.readline().strip()
#	response = ser.read(10)
#       print response
	print response['data']
    except KeyboardInterrupt:
        break

ser.close()
