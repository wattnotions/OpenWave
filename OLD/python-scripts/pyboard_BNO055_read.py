import serial

ser = serial.Serial('COM18', 115200, timeout = 1)


with open('../test_data/pyboard_bno055/bno055_data.csv','w') as f:

    while True:
        f.write(ser.readline().decode())
        