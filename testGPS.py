import Adafruit_BBIO.UART as UART
from GPS import GPS
import time

gps = GPS()

'''
while True:
    print gps.getCoordinates()
    time.sleep(1)
'''
print gps.getCoordinates()

