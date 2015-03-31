import serial
from digimesh import DigiMesh
import Adafruit_BBIO.UART as UART
import time
import os
from multiprocessing import Process
import signal
import sys
from XBee import XBee
from controlScript_class import control
import subprocess

class magProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        execfile("testMag.py")

class controlProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        #execfile("/root/WIPLS/controlScript_timing_Xbee.py")
        subprocess.call(['python', '/root/WIPLS/controlScript_timing_Xbee.py'])

#Create XBee Class
xbee = XBee()

#Initialize Mag and CScript Procees
m = magProcess()
c = controlProcess()


def kill():
    return
    try:
        os.kill(m.pid, signal.SIGKILL)
        #os.kill(m.pid, 9)
        m.join()
        os.kill(c.pid, signal.SIGKILL)
        #os.kill(c.pid, 9)
        c.join()
    except:
        print "none"


f = open('log.txt', 'w')

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
            f.write('process killed\n')
            sys.exit(0)
        elif response == 'mag':
            try:
                m.start()
            except:
                m = magProcess()
                m.start()
        elif 'control' in response:
            #params = response.split(',')
            #First param datapoints, second degrees
            #sys.argv = [params[1]]
            #os.system("python controlScript_timing_Xbee.py")
            f.write('in control if\n')
            execfile("/root/WIPLS/controlScript_timing_Xbee.py")
            '''
            try:
                #control = control()
                #control.start()
                c.start()
                f.write('control process started\n')
            except:
                c = controlProcess()
                c.start()
                f.write('control process except\n')
            ''' 

    except KeyboardInterrupt:
        break
    time.sleep(5)

