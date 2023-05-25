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






while True:


    interface.print_imu_parameters()
    time.sleep(1)
    
  
 
 
    

    """
    accel_data = sensor.acceleration
    if accel_data is not None:
        # Convert the data to string, then to bytes, and send
        accel_data_str = "Accelerometer: {}".format(accel_data)
        print(len(accel_data_str))
        sock.send(bytes(accel_data_str, "utf-8"))
    time.sleep(1)
"""