print("Hello World!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import ssl
import socketpool
import wifi
import board
import adafruit_bno055



print("Connecting to wifi")
wifi.radio.connect('VM5035215', 'v67tjrzjRdje')
print("Connected to 5035")



i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055.BNO055_I2C(i2c)



HOST = "192.168.0.24"
PORT = 8000

# Initialize a socket pool
#pool = socketpool.SocketPool(wifi.radio)
#sock = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
#sock.connect((HOST, PORT))

while True:


    print("Temperature: {} degrees C".format(sensor.temperature))
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Quaternion: {}".format(sensor.quaternion))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print("Gravity (m/s^2): {}".format(sensor.gravity))
    print()
    
  
 
 
    

    """
    accel_data = sensor.acceleration
    if accel_data is not None:
        # Convert the data to string, then to bytes, and send
        accel_data_str = "Accelerometer: {}".format(accel_data)
        print(len(accel_data_str))
        sock.send(bytes(accel_data_str, "utf-8"))
    time.sleep(1)
"""