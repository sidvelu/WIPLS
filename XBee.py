import serial
from digimesh import DigiMesh
import Adafruit_BBIO.UART as UART
import time
import os

class XBee:

    def __init__(self):
        UART.setup("UART2")
        PORT = '/dev/ttyO2'
        BAUD_RATE = 9600
        ser = serial.Serial(PORT, BAUD_RATE)

        if (ser.isOpen()):
            print "its open"

        self.digi = DigiMesh(ser, escaped=True)
        self.XBeeNum = os.environ['XBEE']
        self.DEST_ADDR = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'

    def read(self):
        response = self.digi.wait_read_frame()
        return response['data']

    def send(self, message):
        message = self.XBeeNum + ", " + str(message)
        self.digi.send("tx", dest_addr=self.DEST_ADDR, data = message)
    
