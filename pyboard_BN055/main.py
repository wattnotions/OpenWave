import bno055
from machine import Pin, I2C, UART
import time
from binascii import hexlify


print("......")
print(time.ticks_us())
print(time.ticks_us())
print(time.ticks_us())
print("......")


import micropython
micropython.alloc_emergency_exception_buf(100)

i2c = I2C(1,freq=400000)

timer_flag = 0

tim2 = pyb.Timer(2, freq=100)

ttime = 569029006
linbytes = bytearray(6)

def set_timer_flag(tim2):
    global ttime
    global linbytes
    global timer_flag
    ttime = time.ticks_us()
    i2c.readfrom_mem_into(0x28, 0x28, linbytes)
    timer_flag = 1
    


tim2.callback(set_timer_flag)
s = bno055.BNO055(i2c)





s.load_calibration_data()
print(s.temperature())


test = 0
while(True):

  
    if(timer_flag== 1):
	timer_flag = 0
        #print(linbytes, end = ',')
	print(str(ttime) )
        
  