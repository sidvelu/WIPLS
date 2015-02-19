from xbee import XBee
import serial

'''
with open("xbee_test.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)
'''

ser = serial.Serial('/dev/ttyO2', 9600) # Use UART2 serial port

ser.close()
ser.open()
if ser.isOpen():
    print "its open"

xbee = XBee(ser)

#print(xbee.wait_read_frame())

# Continuously read and print packets
while True:
    try:
        #ser.write('Hello world')
        #response = xbee.wait_read_frame()
        #response = ser.read()
        response = xbee.Receive()
        print response
    except KeyboardInterrupt:
        break

ser.close()
