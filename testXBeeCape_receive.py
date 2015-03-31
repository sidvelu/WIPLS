import time
from xbee import XBee
import serial
import Adafruit_BBIO.UART as UART
from digimesh import DigiMesh

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
#xbee = XBee(ser, escaped=True)
digi = DigiMesh(ser, escaped=True)

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = digi.wait_read_frame()
        print response['data']
    except KeyboardInterrupt:
        break

ser.close()

