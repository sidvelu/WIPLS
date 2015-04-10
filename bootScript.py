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
            kill()
        elif response == 'kill':
            kill()
            #sys.exit(0)
            os.system("shutdown -h now")
        elif response == 'align':
            #os.system("python testMove.py l 90")
            subprocess.Popen("python /root/WIPLS/testMove.py l 90", shell=True)
        elif response == 'control':
            #params = response.split(',')
            #First param datapoints, second degrees
            #sys.argv = [params[1]]
            p =subprocess.Popen("python /root/WIPLS/controlScript.py", shell=True)
            print "returned from subprocess call"
        elif XBeeNum in response:
            if 'up' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py u 10", shell=True)
            elif 'down' in response:
                subprocess.Popen("python /root/WIPLS/testMove.py d 10", shell=True)

    except KeyboardInterrupt:
        break
    time.sleep(5)

