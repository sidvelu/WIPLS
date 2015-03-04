import time
from xbee import XBee
import serial
import Adafruit_BBIO.UART as UART

UART.setup("UART2")

# may need this to init the cape
#echo BB-UART2 > /sys/devices/bone_capemgr.*/slots

PORT = '/dev/ttyO2'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

if (ser.isOpen()):
    print "its open"

# Create API object
xbee = XBee(ser, escaped=True)

DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xC4\x04\x84"

# Continuously read and print packets
while True:
    try:
        print "send data"
    	ser.write("test\n")
        time.sleep(1)
    except KeyboardInterrupt:
        break

ser.close()

