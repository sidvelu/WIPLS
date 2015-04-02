from digimesh import DigiMesh
import time
import serial
import Adafruit_BBIO.UART as UART

UART.setup("UART2")
PORT = '/dev/ttyO2'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

if (ser.isOpen()):
    print "its open"

digi = DigiMesh(ser, escaped=True)
DEST_ADDR_LONG = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'

while True:
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='1, strong angle: 50')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='3, strong angle: 90')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, strong angle: 150')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: GPS NOT WORKING')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: err')
    time.sleep(1)
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='1, strong angle: 10')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='3, strong angle: 110')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, strong angle: 300')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: GPS NOT WORKING')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: bug')
    time.sleep(1)
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='1, strong angle: 30')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='3, strong angle: 160')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, strong angle: 350')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: GPS NOT WORKING')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: crash')
    time.sleep(1)
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='1, strong angle: 40')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='3, strong angle: 220')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, strong angle: 290')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: GPS NOT WORKING')
    digi.send("tx", dest_addr=DEST_ADDR_LONG, data='2, ERROR: fail')
    time.sleep(1)
