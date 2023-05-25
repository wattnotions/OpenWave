import board
import adafruit_bno055
import wifi
import socketpool

class Interfaces:
    def __init__(self):
        
        self.i2c = None
        self.sensor = None
        

    def setup_i2c(self, i2c):
        self.i2c = i2c
        self.sensor = adafruit_bno055.BNO055_I2C(self.i2c)
        
    def setup_wifi(self, wifi_name, wifi_pass):
        print("Connecting to wifi")
        wifi.radio.connect(wifi_name, wifi_pass)
        print("Connected to 5035")
        
        
    def setup_socket(self, host, port):
        pool = socketpool.SocketPool(wifi.radio)
        sock = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
        sock.connect((self.host, self.port))

    def print_imu_parameters(self):
        if self.sensor is not None:
            print("Temperature: {} degrees C".format(self.sensor.temperature))
            print("Accelerometer (m/s^2): {}".format(self.sensor.acceleration))
            print("Magnetometer (microteslas): {}".format(self.sensor.magnetic))
            print("Gyroscope (rad/sec): {}".format(self.sensor.gyro))
            print("Euler angle: {}".format(self.sensor.euler))
            print("Quaternion: {}".format(self.sensor.quaternion))
            print("Linear acceleration (m/s^2): {}".format(self.sensor.linear_acceleration))
            print("Gravity (m/s^2): {}".format(self.sensor.gravity))
            print()
        else:
            print("Sensor not initialized. Please call setup_i2c method first.")
