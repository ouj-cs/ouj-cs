import random
import time
import RPi.GPIO as GPIO
def morse_code():
    return ("A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- "
            "K -.- L .-.. M -- N -. O --- P .--. Q --.- R .-. S ... T - "
            "U ..- V ...- W .-- X -..- Y -.-- Z --..")
def get_dict():
    ss=morse_code().split()
    return dict((key, value) for key,value in zip(ss[0::2],ss[1::2]))
def encode_character(dic,char):
    lis=[]
    for c in dic[char]:
        if c==".":
            lis+=[(0.2,True),(0.2,False)]
        elif c=="-":
            lis+=[(0.6,True),(0.2,False)]
        else:
            assert(False)
    return lis
def encode_string(s):
    lis=[]
    for c in s:
        lis+=encode_character(get_dict(),c)
        lis+=[(0.6,False)]
    return lis
def create_question():
    s=""
    for _ in range(2):
        s+=random.choice(list(get_dict().keys()))
    return s
print(morse_code())

GPIO.setmode(GPIO.BCM)   # Uses GPIO pin numbers.
GPIO.setup(25,GPIO.OUT)  # Uses GPIO #25 as output.
try:
    while True:
        question=create_question()
        code=encode_string(question)
        for length,boolean in code:
            if boolean:
                GPIO.output(25,GPIO.HIGH)
            else:
                GPIO.output(25,GPIO.LOW)
            time.sleep(length)
        print("Your Answer: ",end="")
        s=input()
        if s.upper()==question:
            print("Good.")
        else:
            print("It was",question)
            print(morse_code())
        time.sleep(2)
except KeyboardInterrupt:
    pass  # Terminates program with Ctrl+C.
GPIO.cleanup()  # Initializes GPIO.setup().
print("Done.")