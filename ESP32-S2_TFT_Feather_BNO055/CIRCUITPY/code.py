print("Hello World!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import ssl
import board
import openwave
import digitalio
import storage

interface = openwave.Interfaces()

#interface.setup_wifi('VM5035215', 'v67tjrzjRdje')
interface.setup_i2c(board.I2C())
#interface.socket_connect("192.168.0.24", 8000)




interface.record_linaccel(10, 60)
  
 
 
 