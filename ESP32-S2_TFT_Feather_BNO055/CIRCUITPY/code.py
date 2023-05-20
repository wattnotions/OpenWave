print("Hello World!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import ssl
import socketpool
import wifi
import board
import adafruit_bno055
import digitalio
import microcontroller
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from digitalio import DigitalInOut
import busio


print("Connecting to wifi")
wifi.radio.connect('VM5035215', 'v67tjrzjRdje')
print("Connected to 5035")
### Feeds ###

# List all pins
for pin in dir(board):
    print(pin)

### Code ###

#pin = digitalio.DigitalInOut(board.I2C_POWER)
#pin.direction = digitalio.Direction.OUTPUT
#pin.value=True



# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT





i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_bno055.BNO055_I2C(i2c)

# If you are going to use UART uncomment these lines
# uart = board.UART()
# sensor = adafruit_bno055.BNO055_UART(uart)

last_val = 0xFFFF


def temperature():
    global last_val  # pylint: disable=global-statement
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result


while True:
    print("Temperature: {} degrees C".format(sensor.temperature))
    """
    print(
        "Temperature: {} degrees C".format(temperature())
    )  # Uncomment if using a Raspberry Pi
    """
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Quaternion: {}".format(sensor.quaternion))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print("Gravity (m/s^2): {}".format(sensor.gravity))
    print()
    
    HOST = "192.168.0.24"
    PORT = 8000
 
 
    

    # Initialize a socket pool
    pool = socketpool.SocketPool(wifi.radio)

    # Create a TCP socket
    sock = pool.socket(pool.AF_INET, pool.SOCK_STREAM)

    # Use the socket to connect to the server
    sock.connect((HOST, PORT))

    # Send some data
    sock.send(b'Hello, world!')
    
    time.sleep(1)
