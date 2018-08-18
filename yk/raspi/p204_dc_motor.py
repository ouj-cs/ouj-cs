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

GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
p0=GPIO.PWM(25,50)
p1=GPIO.PWM(24,50)
p0.start(0)
p1.start(0)
adc_pin0=0
try:
    while True:
        inp=read_ad(adc_pin0,SCLK,MOSI,MISO,SS)
        print("inp:",inp)
        if inp>100 and inp<2048:
            p1.ChangeDutyCycle(0)
            duty=(2048-inp)*70/2078
            p0.ChangeDutyCycle(duty)
        elif inp>2048 and inp<4000:
            p0.ChangeDutyCycle(0)
            duty=(inp-2048)*70/2078
            p1.ChangeDutyCycle(duty)
        time.sleep(0.5)  # idle.
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
p0.stop()
p1.stop()
GPIO.cleanup()  # Initializes GPIO.setup().
