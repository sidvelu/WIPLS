import serial
from digimesh import DigiMesh
import Adafruit_BBIO.UART as UART
import time
import os

class XBee:

    def __init__(self):
        UART.setup("UART2")
        PORT = '/dev/tty02'
        BAUD_RATE = 9600
        self.ser = serial.Serial(PORT, BAUD_RATE)

        if (ser.isOpen()):
            print "its open"

        self.digi = DigiMesh(ser, escaped=True)
        self.xBeeNum = os.environ['XBEE']
        self.DEST_ADDR = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'

    def read(self):
        response = digi.wait_read_frame()
        return response['data']

    def send(self, message):
        message = self.XBeeNum + message
        digi.send("tx", dest_addr=DEST_ADDR, data = message)
    



