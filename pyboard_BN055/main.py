import bno055
from machine import Pin, I2C, UART
import time
from binascii import hexlify
import ustruct


print("......")
print(time.ticks_us())
print(time.ticks_us())
print(time.ticks_us())
print("......")


import micropython
micropython.alloc_emergency_exception_buf(100)

i2c = I2C(1,freq=400000)
bt_uart = UART(3, 115200) # connected to bluetooth module

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
    



s = bno055.BNO055(i2c)

time.sleep(1)
tim2.callback(set_timer_flag)



s.load_calibration_data()
print(s.temperature())


test = 0
while(True):

  
    if(timer_flag== 1):
	timer_flag = 0
        data = ustruct.unpack("<hhh", linbytes)    #convert raw bytes to ints
        data = ','.join(map(str,data))              #convert tuple to string
        bt_uart.write(data)                        #write linaccel data
        bt_uart.write(", " + str(ttime) + '\r\n')  #append timestamp
        
  