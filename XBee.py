import serial
from digimesh import DigiMesh
import Adafruit_BBIO.UART as UART
import time
import os
from PanTilt import PanTilt

class XBee:
    def print_data(self, data):
        print data
        if ('kill' in data['data']):  # found kill, exit
            print "KILLING"
            self.tilt.stop()
            os.system('pkill -1 -f controlScript_timing_Xbee.py')

    def __init__(self):
        UART.setup("UART2")
        PORT = '/dev/ttyO2'
        BAUD_RATE = 9600
        self.tilt = PanTilt()
        ser = serial.Serial(PORT, BAUD_RATE)

        if (ser.isOpen()):
            print "its open"

        self.digi = DigiMesh(ser, escaped=True, callback=self.print_data)
        ID_file = open('/root/WIPLS/XBEE_ID', 'r')
        self.XBeeNum = str(ID_file.read())
        ID_file.close()
        print "XBEE NUM: ", self.XBeeNum
        
        self.DEST_ADDR = b'\x00\x00\x00\x00\x00\x00\xFF\xFF'

    def read(self):
        response = self.digi.wait_read_frame()
        return response['data']

    def send(self, message):
        message = self.XBeeNum + ", " + str(message)
        self.digi.send("tx", dest_addr=self.DEST_ADDR, data = message)
    
