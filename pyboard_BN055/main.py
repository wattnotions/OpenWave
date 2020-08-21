import bno055
from machine import Pin, I2C, UART
import time
from binascii import hexlify

i2c = I2C(1,freq=100000)
s = bno055.BNO055(i2c)

def print_linaccel(tim4):
    print(s.linear_acceleration())

tim4 = pyb.Timer(4, freq=10)
tim4.callback(print_linaccel)




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