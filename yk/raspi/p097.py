import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)   # Uses GPIO pin numbers.
GPIO.setup(25,GPIO.OUT)  # Uses GPIO #25 as output.
try:
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
GPIO.cleanup()  # Initializes GPIO.setup().
