import RPi.GPIO as GPIO
import time
def read_ad(channel,SCLK,MOSI,MISO,SS):
    if channel<0 or channel>7:
        return -1
    GPIO.output(SS,GPIO.HIGH)
    GPIO.output(SCLK,GPIO.LOW)
    GPIO.output(SS,GPIO.LOW)
    command=(channel|0x18)<<3  # 11cc c000 in binary.
    for i in range(5):  # forall i in {0, 1, 2, 3, 4}.
        if command&0x80:  # xxxx xxxx & 1000 0000 (Sends from MSB to LSB.)
            GPIO.output(MOSI,GPIO.HIGH)
        else:
            GPIO.output(MOSI,GPIO.LOW)
        command<<=1  # Disposes the MSB which already sent.
        GPIO.output(SCLK,GPIO.HIGH)
        GPIO.output(SCLK,GPIO.LOW)
    value=0
    for i in range(13):  # forall i in in {0, 1, ... 11, 12}.
        GPIO.output(SCLK,GPIO.HIGH)
        GPIO.output(SCLK,GPIO.LOW)
        if i==0:  # null bit.
            pass
        else:
            value<<=1
            if GPIO.input(MISO)==GPIO.HIGH:
                value|=0x1
    GPIO.output(SS,GPIO.HIGH)
    return value
GPIO.setmode(GPIO.BCM)   # Uses GPIO pin numbers.
SCLK=11  # serial clock.
MOSI=10  # master output slave input.
MISO=9   # master input slave output.
SS=8     # slave select.
GPIO.setup(SCLK,GPIO.OUT)
GPIO.setup(MOSI,GPIO.OUT)
GPIO.setup(MISO,GPIO.IN)
GPIO.setup(SS,GPIO.OUT)
try:
    while True:
        input_value=read_ad(0,SCLK,MOSI,MISO,SS)
        print("value:",input_value)
        time.sleep(0.2)  # idle.
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
GPIO.cleanup()  # Initializes GPIO.setup().
