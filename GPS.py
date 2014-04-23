import Adafruit_BBIO.UART as UART
import serial
import time
import datetime as dt


class GPS:

    ser = None

    def __init__(self):
        UART.setup("UART1")
        self.ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600, timeout=1, writeTimeout=1)
        self.ser.close()
        self.ser.open()

        if self.ser.isOpen():
            print "Serial is open!"

    def getCoordinates(self):
        fix = False
        start = dt.datetime.now()
        end = dt.datetime.now()
        while (fix == False and (end-start).microseconds < 1000):
            line = self.ser.readline()
            if "$GPGGA" in line:
                line = line.split(",") # return list split by comma
                message_ID    = line[0]  # message ID
                UTC_time      = line[1]  # UTC time
                latitude_num  = line[2]  # latitude (ddmm.mmmm)
                latitude_dir  = line[3]  # latitude direction (N or S)
                longitude_num = line[4]  # longitude (dddmm.mmmm)
                longitude_dir = line[5]  # longitude direction (E or W)
                #print latitude_num + latitude_dir
                #print longitude_num + longitude_dir
                if latitude_num != "" and latitude_dir != "":
                    fix = True
                    retLatitude = int(latitude_num[0:2]) + (float(latitude_num[2:9]) / 60 );
                    retLongitude = int(longitude_num[0:3]) + (float(longitude_num[3:10]) / 60 );
                    return (retLatitude, latitude_dir,  retLongitude, longitude_dir)
            end = dt.datetime.now()
        return 0

