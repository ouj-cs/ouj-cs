import RPi.GPIO as GPIO
import time
def callback(channel):
    global led_state
    led_state=not led_state
    print("led_state:",led_state)
    if led_state==GPIO.HIGH:
        GPIO.output(25,GPIO.HIGH)    # Lights LED.
    else:
        GPIO.output(25,GPIO.LOW)
GPIO.setmode(GPIO.BCM)   # Uses GPIO pin numbers.
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.OUT,initial=GPIO.LOW)
GPIO.add_event_detect(24,GPIO.RISING,callback=callback,bouncetime=200)
led_state=GPIO.LOW
try:
    while True:
        time.sleep(0.01)  # idle.
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
GPIO.cleanup()  # Initializes GPIO.setup().
