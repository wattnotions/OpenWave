import bno055
from machine import Pin, I2C, UART
import time

i2c = I2C(1,freq=100000)
calib_data = i2c.readfrom_mem(0x28, 0x55, 22)
print(calib_data)
f = open('calibration.bin', 'wb')
f.write(calib_data)
f.close()

time.sleep_ms(500)
f = open("calibration.bin", 'rb')
old_calib = f.read()
print(old_calib)
f.close()

s = bno055.BNO055(i2c)
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