import Adafruit_BBIO.GPIO as GPIO
import time
import sys

pin = "P8_11"

GPIO.setup(pin, GPIO.OUT)

if sys.argv[1] == "high":
    GPIO.output(pin,GPIO.HIGH)
elif sys.argv[1] == "low":
    GPIO.output(pin,GPIO.LOW)
else:
    print "error"

time.sleep(50)
