print("Hello World!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import ssl
import board
import openwave

interface = openwave.Interfaces()

interface.setup_wifi('VM5035215', 'v67tjrzjRdje')
interface.setup_i2c(board.I2C())
interface.socket_connect("192.168.0.24", 8000)






while True:


    interface.print_imu_parameters()
    
    accel_data_str = "Accelerometer: {}".format(interface.sensor.acceleration)
    interface.socket_send(bytes(accel_data_str, "utf-8"))
    time.sleep(1)
    
  
 
 
 