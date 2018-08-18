import smbus
import time
def read_adt7410():
    word=bus.read_word_data(address_adt7410,register_adt7410)
    data=(word & 0xff00)>>8 | (word & 0xff)<<8
    data>>=3
    if data & 0x1000 == 0:  # the temperature >= 0.
        temp=data*0.0625
    else:
        temp=((~data&0x1fff) + 1)*-0.0625
    return temp
bus=smbus.SMBus(1)
address_adt7410=0x48
register_adt7410=0x00
try:
    while True:
        value=read_adt7410()
        print(value)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
