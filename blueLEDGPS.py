from GPS import GPS
import Adafruit_BBIO.GPIO as GPIO
import time


GPS = GPS()


blueLED = "P8_11"
GPIO.setup(blueLED, GPIO.OUT)
GPIO.output(blueLED, GPIO.LOW)
prevLED = 0

while(True):
    GPSFix = GPS.getCoordinates()
    #print GPSFix
    if GPSFix == 0:
        if prevLED == 0:
            GPIO.output(blueLED, GPIO.HIGH)
            prevLED = 1
        else:
            GPIO.output(blueLED, GPIO.LOW)
            prevLED = 0
    else:
        GPIO.output(blueLED, GPIO.HIGH)
    #time.sleep(1)
            
            
        
        
