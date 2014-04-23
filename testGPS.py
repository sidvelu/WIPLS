import Adafruit_BBIO.UART as UART
import serial
 
UART.setup("UART1")
 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=4800)#, timeout=2)
ser.close()
ser.open()
if ser.isOpen():
	print "Serial is open!"
#	ser.write("Hello World!")
#	ser.write("$PSRF100,1,4800,8,1,0*38<CR><LF>")
#	ser.write("$PSRF101,-2686700,-4304200,3851624,96000,497260,921,12,3*7F")
	ser.write("$PSRF103,05,00,01,01*20\r\n")

while ser.isOpen():
	line = ser.readline()  # get a line
	#print line
	if "$GPGGA" in line:
		print line
		line = line.split(",") # return list split by comma
		message_ID    = line[0]  # message ID
		UTC_time      = line[1]  # UTC time
		latitude_num  = line[2]  # latitude (ddmm.mmmm)
		print latitude_num
		latitude_dir  = line[3]  # latitude direction (N or S)
		longitude_num = line[4]  # longitude (dddmm.mmmm)
		print longitude_num
		longitude_dir = line[5]  # longitude direction (E or W)

		#print message_ID + " " + UTC_time
	if "$GPVTG" in line:
		line = line.split(",") # return list split by comma
		print "Heading: ",
		print line[1]
		
