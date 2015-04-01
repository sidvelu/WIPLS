from XBee import XBee
import time

xbee = XBee()

while True:
    xbee.send('strong angle: 50')
    time.sleep(1)
    xbee.send('strong angle: 300')
    time.sleep(1)
    xbee.send('strong angle: 100')
    time.sleep(1)
    xbee.send('strong angle: 200')
    time.sleep(1)
