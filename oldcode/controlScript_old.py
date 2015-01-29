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
import baz

# create process class to control signal script
class myProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        execfile("runSignal.py")

while True:
    # determine heading mode
    if not len(sys.argv) > 1:  # no args, skip heading
        #raw_input("\n\nSkipping heading, press Enter to continue...")
        print("\n\nSkipping heading, continuing...")
    elif sys.argv[1] == "0":  # manual heading
        angle = input('\n\nEnter manual heading: ')
        f = open('magData.txt', 'w')
        f.write(str(angle))
        f.close()
    elif sys.argv[1] == "1":  # take heading samples
        #raw_input("\n\nReady to take heading samples, press Enter to continue...")
        print("\n\nTaking samples...")
        execfile("runHeading.py")

    # get signal data by creating another process
    p = myProcess()
    p.start()
    time.sleep(3)
    os.kill(p.pid, signal.SIGTERM) # kill process after certain amount of time
    p.join()  # wait till process is definitely killed

    # process header and signal data
    execfile("processData_new.py")
    execfile("processData.py")

    # run the stepper
    execfile("runMotor.py")
