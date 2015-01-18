import time
import os
from multiprocessing import Process
import signal
import sys

# load all GNUradio modules here, so we load only once
# to reduce time to take samples
print "Loading GNUradio modules once..."
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
from LSM303 import LSM303
import baz

# create process class to control signal script
class myProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        execfile("GNU_v2.py")

#Setting up compass
compass = LSM303()

while True:
    #Getting Heading
    heading = compass.getHeading() 
    print "Heading: " + str(heading)

    # get signal data by creating another process
    p = myProcess()
    p.start()
    #time.sleep(3)
    #os.kill(p.pid, signal.SIGTERM) # kill process after certain amount of time
    p.join()  # wait till process is definitely killed

    #rename signal files
    os.system("mv signal.bin signal_"+ str(round(heading))+ ".bin")
    os.system("mv passband_sig.bin passband_signal_"+ str(round(heading)) + ".bin")
    
    # run the stepper
    #execfile("runMotor.py")

    
    print("Finished one heading")
    raw_input("Press Enter to Continue")

