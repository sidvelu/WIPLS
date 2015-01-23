import Adafruit_BBIO.UART as UART
import serial
import time
 
UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600, timeout=1, writeTimeout=1)
ser.close()
ser.open()
if ser.isOpen():
    print "Serial is open!"
#   prints information about the antenna
#    ser.write("$PGCMD,33,1*6C\r\n")

filename = raw_input('Enter filename for this tracker: ')
f = open(filename, 'w')
fix = False

for x in range(0, 5):
    if ser.isOpen():
        line = ser.readline()  # get a line
        if "$GPGGA" in line:
            line = line.split(",") # return list split by comma
            message_ID    = line[0]  # message ID
            UTC_time      = line[1]  # UTC time
            latitude_num  = line[2]  # latitude (ddmm.mmmm)
            latitude_dir  = line[3]  # latitude direction (N or S)
            longitude_num = line[4]  # longitude (dddmm.mmmm)
            longitude_dir = line[5]  # longitude direction (E or W)
            print latitude_num + latitude_dir
            print longitude_num + longitude_dir
            if latitude_num != "" and latitude_dir != "":
                fix = True
            f.write(str(latitude_num + latitude_dir) + "\n")
            f.write(str(longitude_num + longitude_dir) + "\n\n")
            #print message_ID + " " + UTC_time
        time.sleep(1)
    
    #   for antenna info
    #    if "$PGTOP" in line:
    #        print line

if fix == False:
    print "No GPS coords recorded, need a fix"
