import serial
from digimesh import DigiMesh
import Adafruit_BBIO.UART as UART
import time
import os
from multiprocessing import Process
import signal
import sys
from XBee import XBee

class magProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        execfile("testMag.py")

class controlProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        execfile("controlScript_timing.py")

#Create XBee Class
xbee = XBee()

#Initialize Mag and CScript Procees
m = magProcess()
c = controlProcess()


def kill():
    try:
        os.kill(m.pid, signal.SIGKILL)
        #os.kill(m.pid, 9)
        m.join()
        os.kill(c.pid, signal.SIGKILL)
        #os.kill(c.pid, 9)
        c.join()
    except:
        print "none"



# Continuously read and print packets
while True:
    try:
        print "waiting"
        response = xbee.read()
        print "read"
        if response == 'start':
            os.system("python /root/WIPLS/bootTest.py")
        elif response == 'stop':
            kill()
        elif response == 'kill':
            kill()
            sys.exit(0)
        elif response == 'mag':
            try:
                m.start()
            except:
                m = magProcess()
                m.start()
        elif 'Control' in response:
            params = response.split(',')
            sys.argv = [params[1], params[2]]
            try:
                c.start()
            except:
                c = controlProcess()
                c.start()

    except KeyboardInterrupt:
        break
    time.sleep(5)

