import bno055
from machine import Pin, I2C

i2c = I2C(1,freq=100000)


s = bno055.BNO055(i2c)
print(s.temperature())
print(s.euler())









