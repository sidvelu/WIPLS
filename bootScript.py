import time
import os
import signal
import sys
from XBee import XBee
import subprocess
from PanTilt import PanTilt
import Adafruit_BBIO.GPIO as GPIO

#Create XBee Class
xbee = XBee()


# turn on blue LED
blueLED = "P8_11"
GPIO.setup(blueLED, GPIO.OUT)
GPIO.output(blueLED, GPIO.HIGH)

# get XBee ID
ID_file = open('/root/WIPLS/XBEE_ID', 'r')
XBeeNum = str(ID_file.read()).strip()
ID_file.close()

def kill():
    os.system('pkill -f controlScript.py')
    os.system('pkill -f testMove.py')
    os.system('pkill -f streamMag.py')
    panTilt = PanTilt()
    panTilt.stop()

subprocess.Popen("python /root/WIPLS/blueLEDGPS.py", shell=True)

# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = xbee.read()


        print "read"
        if response == 'stop':
            print "Killing Scripts"
            kill()
        elif response == 'mag':
            print "Streaming mag Values"
            subprocess.Popen("python /root/WIPLS/streamMag.py", shell=True)
        elif response == 'kill':
            kill()
            #sys.exit(0)
            os.system("shutdown -h now")
        elif response == 'align':
            #os.system("python testMove.py l 90")
            subprocess.Popen("python /root/WIPLS/testMove.py l 90", shell=True)
        elif 'control' in response:
            print response
            params = response.split(',')
            #params = response.split(',')
            #First param datapoints, second degrees
            #sys.argv = [params[1]]

            output = "python /root/WIPLS/controlScript.py " + params[1]
            #print output
            #p =subprocess.Popen("python /root/WIPLS/controlScript.py", shell=True)
            p =subprocess.Popen(output, shell=True)
            print "returned from subprocess call"
        elif XBeeNum in response:
            if 'up' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py u 10", shell=True)
            elif 'down' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py d 10", shell=True)
            elif 'left' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py l 10", shell=True)
            elif 'right' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py r 10", shell=True)

    except KeyboardInterrupt:
        break
    time.sleep(5)

