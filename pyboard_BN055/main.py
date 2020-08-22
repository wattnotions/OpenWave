import bno055
from machine import Pin, I2C, UART
import time
from binascii import hexlify


import micropython
micropython.alloc_emergency_exception_buf(200)

i2c = I2C(1,freq=100000)

timer_flag = 0

tim2 = pyb.Timer(2, freq=10)

def set_timer_flag(tim2):
    print("in interrupt")
    


tim2.callback(set_timer_flag)
s = bno055.BNO055(i2c)




s.load_calibration_data()
print(s.temperature())

test = 1

while(True):
    if(test == 1):
        print("test = 1")
    else:
        print("test = 0")