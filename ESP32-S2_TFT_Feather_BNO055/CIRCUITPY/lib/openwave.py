import board
import adafruit_bno055
import wifi
import socketpool
import time

class Interfaces:
    def __init__(self):
        
        self.i2c = None
        self.sensor = None
        self.pool = socketpool.SocketPool(wifi.radio)
        self.sock = self.pool.socket(self.pool.AF_INET, self.pool.SOCK_STREAM)
        self.port=None
        self.host=None
        
        

    def setup_i2c(self, i2c):
        self.i2c = i2c
        self.sensor = adafruit_bno055.BNO055_I2C(self.i2c)
        
    def setup_wifi(self, wifi_name, wifi_pass):
        print("Connecting to wifi")
        wifi.radio.connect(wifi_name, wifi_pass)
        print("Connected to 5035")
        
        
    def socket_connect(self, host, port):
    
        self.host = host
        self.port = port
    
        try:
            self.sock.connect((self.host, self.port))
        except Exception as e:
            print(e)
            
    def socket_send(self, data):
        try:
            self.sock.send(bytes(data, "utf-8"))
        except Exception as e:
            print(e)
            print("attempting socket reconnect....")
            self.socket_connect(self.host, self.port)

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
            
            
    def record_linaccel(self, sample_rate, duration):
        if self.sensor is None:
            print("Sensor not initialized. Please call setup_i2c method first.")
            return

        # Create file name based on current time
       

        start_time = time.time()
        end_time = start_time + duration
        sample_interval = 1.0 / sample_rate

        next_sample_time = start_time

        with open("accel.csv", "w") as f:
            while time.time() < end_time:
                # If it's time for the next sample...
                if time.time() >= next_sample_time:
                    # Write a sample to the file
                    f.write(str(self.sensor.linear_acceleration))
                    f.write('\n')

                    # Schedule the next sample
                    next_sample_time += sample_interval

                # Compute and print progress bar
                elapsed_time = time.time() - start_time
                progress = elapsed_time / duration
                progress_bar = '[' + '='*int(progress*20) + ' '*(20-int(progress*20)) + ']'
                print(f"Recording: {progress_bar} {int(progress*100)}%", end='\r')

        print()  # Finish the line for the progress bar
