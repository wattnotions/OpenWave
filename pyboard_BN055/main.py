import bno055
from machine import Pin, I2C, UART
import time
from binascii import hexlify

import micropython
micropython.alloc_emergency_exception_buf(100)

i2c = I2C(1,freq=100000)



    

tim4 = pyb.Timer(4, freq=10)
s = bno055.BNO055(i2c, tim4)




s.load_calibration_data()
print(s.temperature())



uart = UART(3, 115200)                         # init with given baudrate




#while True:
#    uart.write('hello\r\n')
#    print("Sent hello")
#    time.sleep(1)


#while True:
#    print(s.euler(), end='\r')
#    time.sleep_ms(100)
#    print('\x1b[2K\r', end='')