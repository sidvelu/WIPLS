import time
import os
import signal
import sys
from XBee import XBee
import subprocess
from PanTilt import PanTilt

#Create XBee Class
xbee = XBee()


def kill():
    os.system('pkill -f controlScript_timing_Xbee.py')
    panTilt = PanTilt()
    panTilt.stop()

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
            sys.exit(0)
        elif response == 'control':
            #params = response.split(',')
            #First param datapoints, second degrees
            #sys.argv = [params[1]]
            subprocess.Popen("python /root/WIPLS/controlScript_timing_Xbee.py", shell=True)
            print "returned from subprocess call"

    except KeyboardInterrupt:
        break
    time.sleep(5)

