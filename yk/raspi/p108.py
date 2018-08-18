import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)   # Uses GPIO pin numbers.
GPIO.setup(24,GPIO.IN)   # Uses GPIO #25 as input.
GPIO.setup(25,GPIO.OUT)  # Uses GPIO #25 as output.
try:
    while True:
        if GPIO.input(24)==GPIO.HIGH:  # if GPIO#24 is high.
            GPIO.output(25,GPIO.HIGH)  # Lights LED.
        else:
            GPIO.output(25,GPIO.LOW)
        time.sleep(0.01)  # idle.
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
GPIO.cleanup()  # Initializes GPIO.setup().
